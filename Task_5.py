mass_dict_uniq = {'G': 57, 'A': 71, 'S': 87, 'P': 97,
                  'V': 99, 'T': 101, 'C': 103, 'I/L': 113,
                  'N': 114, 'D': 115,  'K/Q': 128, 'E': 129,
                  'M': 131, 'H': 137, 'F': 147, 'R': 156,
                  'Y': 163, 'W': 186}


mass_min = sorted(mass_dict_uniq.values())[0]


def peptides_count(given_mass):
    amounts_dict = {0: 1}
    for submass in range(mass_min, given_mass+1):
        peptides(submass, amounts_dict)
    if given_mass in amounts_dict:
        return amounts_dict[given_mass]
    return 0


def peptides(submass, amounts_dict):
    for acid_mass in mass_dict_uniq.values():
        if submass - acid_mass in amounts_dict:
            if submass in amounts_dict:
                amounts_dict[submass] = amounts_dict[submass - acid_mass] + amounts_dict[submass]
            else:
                amounts_dict[submass] = amounts_dict[submass - acid_mass]


given_mass = int(input())
print(peptides_count(given_mass))
