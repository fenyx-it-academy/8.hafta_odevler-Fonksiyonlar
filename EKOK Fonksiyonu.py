"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
"""
def ebob(sayi1,sayi2):
    en_buyuk=0
    for i in range(1,sayi1+1):
        if sayi1%i==0 and  sayi2%i==0:
            en_buyuk=i
    return  en_buyuk

def okek():
    sayi1=int(input("1.sayi"))
    sayi2=int(input("2.sayi"))
    okek=(sayi1*sayi2)/ebob(sayi1,sayi2)
    print(okek)
    return okek
okek()
