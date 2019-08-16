#bu kad 1den 1000 kadar olan mukemmel sayilari bulur.

''''''

    #bu kod bir sayinin tam bolenlerini bulur
def tambolenler(sayi):
    bolenler = []  # tam bolenleri icine atmak icin bos bir liste olusturur
    for i in range(1, sayi+1):  # 1 ve sayi dahil bu araliktaki sayilara bakar
        if sayi % i == 0:  # bu araliktaki tam bolen sayilari bulur
            bolenler.append(i)  # tam bolen sayilari bolenler listesinde biriktirir
    return bolenler


def liste_eleman_toplam(liste):     #bu fonk. liste elemanlari icindeki integer lari toplama fonksiyonudur
    toplam=sum(liste)               #listenin butun elemanlarini topluyor
    return toplam                   #toplamin sonucunu donduruyor


mukemmelsayilist=[]                     #kod buldugu mukemmel sayilari bu listede biriktirecek.
for i in range(1000):                   #0-1000 arasindaki sayilari inceliyor

    if liste_eleman_toplam(tambolenler(i))==i*2:    #tambolenleri toplami sayinin 2 kati olmali(
                                                    # sayinin kendisi tam bolenler listesi icinde)
        mukemmelsayilist.append(i)                  #bulunan her mukemmel sayi listeye ekleniyor
print(mukemmelsayilist)
print("Sayilari mukemmel sayilardir.")


