# Bir sayinin tam bolenlerini bulan fonksiyon yazınız.

#Bir sayının pozitif ve tamsayı bölenlerini bulmak

def tamBolenleri(sayi):
    #tam bolenleri atayacagimiz bir liste olusturduk
    tamBolenler = list()
    #2den baslayarak girilen sayiya kadarki tum sayilarin
    #kendisiyle tam bolunup bolunmedigini kontrol etmek icin bir dongu olusturduk
    for i in range(2, sayi ):
        if sayi % i == 0:
            #kendisine tam bolunebilenleri listeye ekledik
            tamBolenler.append(i)
    return tamBolenler


try:
    while True:
        sayi = input("Bir Sayi Giriniz :")
        if sayi == "q":
            print("Program Sonlandiriliyor...")
            break
        elif sayi.isdigit() == True:
            # girilen deger eger rakamlardan olusuyorsa asagidaki islemler yapilir
            # input string oldugu icin inte cevirdik
            sayi = int(sayi)
            if sayi == "q":
                print("Program Sonlandiriliyor...")
                break
            else:
                print("{} sayisinin tam bolenleri: {}".format(sayi, tamBolenleri(sayi)))
        else:
            print('Hatali giris yaptiniz. Lutfen sayi girin!')
except:
    print('Hatali islem. Program sonlandirildi..')