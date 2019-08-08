# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
# Örnek: 97 ---------> Doksan Yedi

okunusDict = {'0':'','1':"Bir",'2':"İki", '3':"Üç", '4':"Dört",
              '5':"Beş", '6':"Altı", '7':"Yedi", '8':"Sekiz", '9':"Dokuz",
             '10':"On",'20':"Yirmi", '30':"Otuz", '40':"Kırk", '50':"Elli",
              '60':"Altmış", '70':"Yetmiş", '80':"Seksen", '90':"Doksan"}

def okunus(sayi):
    #sayidan, sayinin 10a bolumunden kalanini
    #cikartarak birinci okunacak sayiyi bulduk
    birinci = sayi - (sayi % 10)

    #sayinin 10a bolumunden kalani ile de
    #ikinci okunacak sayiyi bulduk
    ikinci = sayi % 10

    #buldugumuz sayilarin sozlukteki okunuslarini yazdiriyoruz
    return okunusDict[str(birinci)]+' '+okunusDict[str(ikinci)]

try:
    while True:
        sayi = input("Lutfen Iki Basamakli Bir Sayi Girin:")

        if sayi.isdigit() == True and len(sayi) <= 2:
            # girilen deger eger rakamlardan olusuyorsa ve sayi uzunlugu
            # 2ye esit ya da kucuk ise asagidaki islemler yapilir

            sayi = int(sayi) # input string oldugu icin inte cevirdik
            print("Yazdiginiz Sayinin Okunusu: {} ".format(okunus(sayi)))
        elif sayi == 'q':
            print("Program Sonlandiriliyor..")
        else:
            print("Hatali giris! Lutfen tek ya da 2 basamakli bir sayi girin:")
            continue
except:
    print('Hatali islem. Program sonlandirildi.. ')



