#Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf
# sayılarının veren bir fonksiyon yazınız.
def buyuk_kucuk_harf(metin=input('metin giriniz:')):
    sayac1=0
    sayac2=0
    sayac3=0
    for sayac in metin:
        if sayac.islower():#kucuk harf kontrolu
            sayac1+=1
        if sayac.isupper():#buyuk harf kontrolu
            sayac2+=1
        if sayac.isdigit():#rakam kontrolu
            sayac3+=1
    print("metinde {} adet buyuk harf,{} adet kucuk harf {} adet rakam bulunur".format(sayac2,sayac1,sayac3))

buyuk_kucuk_harf()
