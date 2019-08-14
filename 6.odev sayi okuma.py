##6. Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir
##fonksiyon yazın.
##Örnek: 97 ---------> Doksan Yedi

tekrakamlar={"1":"Bir","2":"Iki","3":"Uc","4":"Dort","5":"Bes","6":"Alti","7":"Yedi","8":"Sekiz","9":"Dokuz"}
ciftrakamlar={"10":"On","20":"Yirmi","30":"Otuz","40":"Kirk","50":"Elli","60":"Altmis","70":"Yetmis","80":"Seksen","90":"Doksan"}

#sadece iki haneli sayilar icin yazildi!!
def sayiokuma(sayi):
    if len(sayi)==2:
        coz=[*sayi]
        onluk=int(coz[0])*10
        birlik=int(coz[1])
        oku=(ciftrakamlar.get(str(onluk)),tekrakamlar.get(str(birlik)))
        print(*oku)
        return (oku)
#get fonksiyonu ile sozluklerdeki anahtar kelimelerden hareketle degerleri bulduk
    else:
        print("Lutfen yalnizca iki haneli sayi giriniz")
sayiokuma(sayi=input("iki basamakli bir sayi giriniz :"))
