dna_string = input()
peptide = input()

RNA_table = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T',
             'ACU': 'T', 'AGA': 'R', 'AGC': 'S', 'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I',
             'AUG': 'M', 'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H', 'CCA': 'P',
             'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
             'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
             'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 'GGA': 'G', 'GGC': 'G',
             'GGG': 'G', 'GGU': 'G', 'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAA': '',
             'UAC': 'Y', 'UAG': '', 'UAU': 'Y', 'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
             'UGA': '', 'UGC': 'C', 'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L',
             'UUU': 'F'}


def transcribe(acid_string, mode_from, mode_into):
    """Transcribe acid_string by changing Timine and Uracile"""
    if mode_from == 'rna' and mode_into == 'dna':
        string = acid_string.replace('U', 'T')
    elif mode_from == 'dna' and mode_into == 'rna':
        string = acid_string.replace('T', 'U')
    else:
        raise ValueError('Incorrect mode')
    return string


def complement(acid_string, reverse=False):
    """Find a complement or reverse complement for acid_string"""
    result_acid = []
    for symbol in acid_string:
        if symbol == 'G':
            result_acid.append('C')
        elif symbol == 'C':
            result_acid.append('G')
        elif symbol == 'A':
            result_acid.append('T')
        elif symbol == 'T':
            result_acid.append('A')
        else:
            raise ValueError('Incorrect complement')
    if reverse:
        result_acid.reverse()
    string = ''.join(result_acid)
    return string


def decode(dna_string):
    """Find all amino acid sequences which encode given DNA string"""
    # complement
    reversed_complement = complement(dna_string, reverse=True)

    # transcription
    transcribed = (transcribe(dna_string, 'dna', 'rna'), transcribe(reversed_complement, 'dna', 'rna'))

    # translation
    peptides = tuple([translate(item) for item in transcribed])
    return peptides


def translate(string):
    """Split string of nucleotides on triplets and translate it into Peptides"""
    triplets = []
    while string:
        triplets.append(string[:3])
        string = string[3:]
    acid_string = ''
    for rna_pattern in triplets:
        if rna_pattern in RNA_table:
            acid_string = acid_string + RNA_table[rna_pattern]
    return acid_string


def brute(dna_string, peptide):
    sequence_length = len(peptide) * 3
    found = []
    for i in range(len(dna_string)-sequence_length + 1):
        subseq = dna_string[i:i + sequence_length]
        if peptide in decode(subseq):
            found.append(dna_string[i:i+sequence_length])
    return found


for i in brute(dna_string, peptide):
    print(i)