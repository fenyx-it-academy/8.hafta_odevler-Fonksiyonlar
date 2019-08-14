##9. Kullanıcıdan bir input alan ve bu inputun içindeki
##büyük ve küçük harf sayılarının veren bir fonksiyon yazınız.
buyukharfler=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','V','Y','Z','X']
kucukharfler=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','y','z','x']
buyuk_harfler=[]
kucuk_harfler=[]
diger=[]
def harf_sayisi():
    kul=input("Bir metin giriniz : ")
    global buyuk_harfler
    global kucuk_harfler
    for i in kul:
        if i in buyukharfler:
            buyuk_harfler += [str(i)]
        if i in kucukharfler:
            kucuk_harfler += [str(i)]
    print("Buyuk harf sayisi : ",len(buyuk_harfler), "\n" ,"Kucuk harf sayisi : " ,len(kucuk_harfler),sep="")
harf_sayisi()                
 
## global ile fonksiyon icerisindeki degiskenlerin global alanda kullanilmasini sagladik
