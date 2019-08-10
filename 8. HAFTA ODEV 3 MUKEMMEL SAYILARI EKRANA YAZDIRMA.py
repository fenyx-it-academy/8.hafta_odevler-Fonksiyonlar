#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
#Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
#Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).


print("Mükemmel Sayılar")

def mukemmelsayi(sayi) :
    bolen_toplam = 0

    for i in range(1, sayi):
        if (sayi % i) == 0:
            bolen_toplam += i

    return sayi == bolen_toplam

for i in range(1,1001) :
    if mukemmelsayi(i) :
        print(i)
