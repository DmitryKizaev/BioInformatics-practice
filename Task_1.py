from re import findall
# pattern = 'ATAT'
# genome = 'GATATATGCATATACTT'

pattern = input()
genome = input()

number = len(findall(r'(?=(' + pattern + '))', genome))
print(number)
