##Bir sayinin tam bolenlerini bulan fonksiyon yazınız.
BolunebilenListe = []
def Bolunebilenler(kul):
#sayinin kendisinide alabilmek icin 1 ekledik. cunku range son degeri almaz
    for i in range(1,kul+1):
        if kul % i == 0:
#burada BolunebilenListe += [str(i)] de kullanabiliriz
            BolunebilenListe.append(i)
# return if icerisine yazildiginda calismiyor!!
    return BolunebilenListe
print(Bolunebilenler(int(input("rakam gir : "))))


    
