
def obeb(sayi1, sayi2):
    for i in range(int(sayı1), 0, -1):
        if sayi1 % i == 0 and sayi2 % i == 0:
            break
    return i


sayı1 = int(input("bir sayı giriniz:"))
sayı2 = int(input("bir sayhı giriniz:"))
print(obeb(sayı1, sayı2))

def okek(sayi1,sayi2):

    okek=(sayi1*sayi2)/obeb(sayi1,sayi2)
    print(okek)

    return okek


sayı1 = int(input("bir sayı giriniz:"))
sayı2 = int(input("bir sayhı giriniz:"))
okek(sayı1,sayı2)
