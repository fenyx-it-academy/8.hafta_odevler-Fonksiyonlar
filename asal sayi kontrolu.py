#bu kod bir sayinin asal olup oladigina bakar
'''once sayiyi tam(kalansiz) bolen sayilarin listesini yapar.bu listenin sadece 1 ve kendisinden olusmasi durumunda
sayinin asal oldugunu yazdirir.eger daha fszla tam boleni varsa asal olmadigini yazdirir'''


    #bu kod bir sayinin tam bolenlerini bulur
def tambolenler(sayi):
    bolenler = []  # tam bolenleri icine atmak icin bos bir liste olusturur
    for i in range(1, sayi+1):  # 1 ve sayi dahil bu araliktaki sayilara bakar
        if sayi % i == 0:  # bu araliktaki tam bolen sayilari bulur
            bolenler.append(i)  # tam bolen sayilari bolenler listesinde biriktirir
    return bolenler

while True:
    a=input("Asal olma durumunu kontrol etmek istediginiz sayiyi giriniz(cikmak icin q):")

    #asal sayi kontrolu icin kullanicidan sayi istenir

    if a=='q':                  #sorgulamadan cikis yapmak icin bu blok kullanilir
        break
    elif a.isdigit()==False:                             #sayi haricinde bir veri girilirse
        print('sayi girdiginizden emin misiniz!!')       #uyari
    elif tambolenler(int(a))==[1,int(a)]:                           #kendisi ve 1 den baska boleni olmamali.
        print(tambolenler(int(a)))                               #tambolen sayilarin listesini basar.
        print("{} sayisi bir asal sayidir. ".format(int(a)))     #asal sayi olup olmadigini bildirir
    else:
        print(tambolenler(int(a)))                                #tambolen sayilarin listesini basar.
        print("{} sayisi asal degildir".format(int(a)))           #asal sayi olup olmadigini bildirir