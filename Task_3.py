# if we write the cycle two times to put it into a string:
# NQELnqel
# there will be (len(string)-1) variants of subpeptide length:
# "N" - length 1, "NQ" - length 2, "NQE" - length 3
# and we will also have len(string) possible variants of starting position for each length value:
# let length be 3, the variants are:
# NQE, QEL, ELn, Lnq
# after "Lnq" goes "nqe" which is already mentioned (it is a second row in a cycle)
# so totally we have len(string) * (len(string)-1) possible subpeptides.

length = int(input())
print(length * (length - 1))