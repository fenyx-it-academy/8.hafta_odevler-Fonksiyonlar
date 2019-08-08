""" 1. soru """
""" Asal sayi olup olmadigini kontrol eden fonksiyon yazınız."""
def asal_sayi(number):
    sayac=0
    for i in range(2,number):
        if number%i==0 :
             sayac+=1
    if sayac!=0:
        return "sayi asal degildir"
    return "sayi asaldir"

print(asal_sayi(24))


""" 2. soru """
"""Bir sayinin tam bolenlerini bulan fonksiyon yazınız."""

def tam_bolen(number):
    bolenler=[]
    for i in range(1,number):
        if number%i==0 :
             bolenler.append(i)

    return bolenler

print(tam_bolen(24))


""" 3. soru """
"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının, kendisi haric pozitif tam bolenleri toplami o sayiya esit ise mukemmel sayidir.
 Örnek olarak 28 mükemmel bir sayıdır (1+2+4+7+14=28)."""

def mukemmel_sayi(sayi):
    toplam=0
    for i in range(1,sayi):
        if sayi%i==0:
            toplam+=i
    if toplam==sayi:
        return "sayi mukemmeldir"
    return "sayi mukemmel degildir"
print(mukemmel_sayi(28))


""" 4. soru """

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


""" 5. soru """

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


""" 6. soru """

"""
 Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
 Örnek: 97 ---------> Doksan Yedi
"""

def okunus():
    birler_basamagi=[" ", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]
    onlar_basamagi=["on","yirmi", "otuz", "kirk", "elli", "altmis", "yetmis", "seksen", "doksan"]
    sayi=input("sayiyi giriniz:")
    return  onlar_basamagi[int(sayi[0])-1]+" " +  birler_basamagi[int(sayi[1])]

print(okunus())


""" 7. soru """

""" 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)"""

from math import sqrt

def pisagor():
    ucgenler=[]
    ucgen=[]

    for i in range(1,101):
        for j in range(1,101):
            c=i**2 + j**2
            ucuncu_kenar = sqrt(c )
            if  int(ucuncu_kenar)== ucuncu_kenar and ucuncu_kenar<100 :
                ucgen.append(i)
                ucgen.append(j)
                ucgen.append(ucuncu_kenar)
        ucgenler.append(ucgen)

    return ucgenler
print(pisagor())


""" 8. soru """

""" Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız."""
def faktoriyel(sayi):
    faktoriyel=1
    for i in range(1,sayi+1):
        faktoriyel*=i
    return faktoriyel
print(faktoriyel(30))

""" 9. soru """

"""
 Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf sayılarının veren bir fonksiyon yazınız.
"""
def buyuk_kucuk_harf():
    buyuk=0
    kucuk=0
    kelime=input("Lutfen buyuk/kucuk harf iceren bir kelime giriniz:")
    for i in kelime:
       if  i.islower()==True:
           kucuk+=1
       elif i.isupper()==True:
           buyuk+=1
    sonuc="buyuk harf sayisi:"+str(buyuk)+"kucuk harf sayisi:"+str(kucuk)
    return sonuc

print(buyuk_kucuk_harf())


""" 10. soru """

"""
 Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve
sonrasında bu kelimeleri harf sırasına göre dizip tekrar tire ile ayırıp output olarak veren bir fonksiyon yazınız.
örnek girdi: green-red-yellow-black-white örnek çıktı: black-green-red-white-yellow
"""

def kelime_siralama():
    kelime_sirasi= input("Lutfen (-)Tire ile ayirarak birden fazla kelime giriniz:")
    kelimeler=kelime_sirasi.split("-")
    kelimeler.sort()
    print(*kelimeler,sep="-")

kelime_siralama()


""" 11. soru """
"""
 Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
Örnek Liste :  Özgün Liste : [1, 2, 3, 4, 5]
"""
def ozgun_eleman():
    liste=[1,2,3,3,3,3,4,5,5]
    yeni_liste=[]
    for i in liste:
        if i not in yeni_liste:
            yeni_liste.append(i)
    return yeni_liste
print(*ozgun_eleman())

""" 12. soru """

"""
12. Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız.
örnek: madam, tacocat, utrecht sonuç: True, True, False
"""
def tersi(*args):
    kelime_ters=""
    sonuc=[]
    for i in args:
        for j in range(len(i)-1,-1,-1):
            kelime_ters+=i[j]
        print(kelime_ters)
        if i==kelime_ters:
            sonuc.append(True)
            kelime_ters = ""

        else:
            sonuc.append(False)
            kelime_ters = ""

    return sonuc




print(tersi( "madam", "tacocat", "utrecht", "ama"))





