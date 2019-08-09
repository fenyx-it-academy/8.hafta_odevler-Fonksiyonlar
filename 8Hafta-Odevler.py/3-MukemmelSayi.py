"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)"""
def mukemmmelsayi(sayi):
    tam_bolen = 0
    for i in range(1,sayi):
        if sayi%i == 0:#tam bolenlerini bulup  tam_bolen degiskenimize gonderiyoruz
            tam_bolen+=i
    return tam_bolen == sayi#sayinin tam bolen toplami kendisine esitse bu degeri dondur
a = []
for i in range(1,1001):#1000 dahil 1 ile 1000 arasindaki mukemmel sayilar icin dongu olusturduk
    if mukemmmelsayi(i):#sayi mukemmel sayi ise bos listemize ekle
        a.append(i)
print("1 ile 1000 arasindaki mukemmel sayilar",a)