"""8. Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız."""
def faktoriyel(sayi):
    faktoriyel=1
    for i in range(1,sayi+1):
        faktoriyel*=i
    return faktoriyel
print(faktoriyel(30))
