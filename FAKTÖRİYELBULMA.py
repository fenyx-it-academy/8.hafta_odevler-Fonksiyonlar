"""Pozitif bir tamsayının faktöriyelini alan
 bir fonksiyon yazınız."""

def fak (sayi):
    fakt=1

    for i in range (1,sayi+1):
        fakt*=i
    return fakt
print("Faktöriyeli: ", fak(6))