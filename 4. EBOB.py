# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

def ebobBul(sayi1,sayi2):

    sayi1Bolenleri = []
    sayi2Bolenleri = []
    ortakBolenler = []

    for i in range(1, sayi1+1):
        if sayi1 % i == 0:
            #Girilen ilk sayinin tam bolenlerini listeye ekledik
            sayi1Bolenleri.append(i)
    for j in range(1, sayi2 + 1):
        if sayi2 % j == 0:
            #Girilen ikinci sayinin tam bolenlerini listeye ekledik
            sayi2Bolenleri.append(j)

    for k in sayi1Bolenleri:
        for l in sayi2Bolenleri:
            if k == l:
                #iki liste icerisindeki esit olan sayilari ortak bir listeye aktardik
                ortakBolenler.append(k)
    n = 0
    for m in ortakBolenler:
        # ortak bolenler icindeki en buyuk sayiyi buluyoruz
        if m > n:
            ortakBolenlerinEnBuyugu = m
        n = m

    print("Birinci Sayinin Tam Bolenleri :", sayi1Bolenleri)
    print("Ikinci Sayinin Tam Bolenleri:", sayi2Bolenleri)
    print("Ortak Bolenler:", ortakBolenler)
    print("Ortak Bolenlerin En Buyugu:", ortakBolenlerinEnBuyugu)

try:
    while True:
        sayi1 = input("1.sayiyi girin: ")
        sayi2 = input("2.sayiyi girin: ")

        if sayi1 == "q" or sayi2 == "q":
            print("Program Sonlandiriliyor...")
            break
        elif sayi1.isdigit() == True and sayi2.isdigit() == True:
            # girilen deger eger rakamlardan olusuyorsa asagidaki islemler yapilir
            # input string oldugu icin inte cevirdik
            sayi1 = int(sayi1)
            sayi2 = int(sayi2)
            ebobBul(sayi1, sayi2)
        else:
            print('Hatali giris yaptiniz. Lutfen sayi girin!')
except:
    print('Hatali islem. Program sonlandirildi.. ')
