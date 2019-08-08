# 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
# Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
# Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
# Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)


def mukemmelSayiMi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            #sayinin tam bolenlerini toplam degiskeninde topluyoruz
            toplam += i
    if toplam == sayi:
        #sayi, eger kendi tam bolenlerinin toplamina esitse true doner
        return True
try:
    while True:
        sayi = input("Bir sayi girin: ")

        if sayi == "q":
            print("Program Sonlandiriliyor...")
            break
        elif len(sayi) > 6:
            print('En fazla 6 basamakli bir sayi girebilirsiniz!')
        elif sayi.isdigit() == True :
            # girilen deger eger rakamlardan olusuyorsa asagidaki islemler yapilir
            # input string oldugu icin inte cevirdik
            sayi = int(sayi)
            if mukemmelSayiMi(sayi) == True:
                print("{} sayisi mukemmel sayidir.".format(sayi))
            else:
                print("{} sayisi mukemmel sayi degildir.".format(sayi))
        else:
            print('Hatali giris yaptiniz. Lutfen sayi girin!')
except:
    print('Hatali islem. Program sonlandirildi.. ')
