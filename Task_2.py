# text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
# k = 4

text = input()
k = int(input())

k_mers_dict = {}

for i in range(len(text)):
    k_mer = text[i:i + k]
    if k_mer not in k_mers_dict.keys():
        k_mers_dict[k_mer] = 1
    else:
        k_mers_dict[k_mer] += 1

max_freq = 0
max_freq_k_mers = []

for k_mer, freq in zip(k_mers_dict.keys(), k_mers_dict.values()):
    if freq > max_freq:
        max_freq_k_mers = []  # clear list if found more frequent k-mer
        max_freq = freq
        max_freq_k_mers.append(k_mer)
    elif freq == max_freq:
        max_freq_k_mers.append(k_mer)

for item in max_freq_k_mers:
    print(item)
