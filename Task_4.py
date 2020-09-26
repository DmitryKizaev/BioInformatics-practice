# peptide = 'LEQN'
peptide = input()

mass_dict = {'G': 57, 'A': 71, 'S': 87, 'P': 97,
             'V': 99, 'T': 101, 'C': 103, 'I': 113,
             'L': 113, 'N': 114, 'D': 115,  'K': 128,
             'Q': 128, 'E': 129, 'M': 131, 'H': 137,
             'F': 147, 'R': 156, 'Y': 163, 'W': 186}

cycled = peptide + peptide

subpeptides = []
for length in range(1, len(peptide)):
    for offset in range(len(peptide)):
        subpeptides.append(cycled[offset:offset + length])

subpeptides.append(peptide)
subpeptides.append('')

cyclospectrum = []
for item in subpeptides:
    value = 0
    for letter_id in range(len(item)):
        if item[letter_id] in mass_dict:
            value += mass_dict[item[letter_id]]
    cyclospectrum.append(value)

cyclospectrum.sort()
for mass in cyclospectrum:
    print(mass, end=" ")
