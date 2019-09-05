

def faktoriyelbulmaislemi(sayi):

    faktoriyel = 1

    for i in range(2, sayi + 1):
        faktoriyel *= i
    return faktoriyel


sayi = int(input("Sayi giriniz: "))
print(faktoriyelbulmaislemi(sayi))



