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

base = input()
modified = complement(base, reverse=True)
print(modified)
