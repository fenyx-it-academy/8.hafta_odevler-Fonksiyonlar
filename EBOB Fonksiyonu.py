"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
"""
def ebob():
    sayi1=int(input("1.sayi"))
    sayi2=int(input("2.sayi"))
    en_buyuk=0
    for i in range(1,sayi1+1):
        if sayi1%i==0 and  sayi2%i==0:
            en_buyuk=i
    return "en buyuk ortak bolen", en_buyuk

print(ebob())