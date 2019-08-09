# coding=utf-8
def pisagor(veri):
    # fonksiyon ve parametre tanımlama
    sayac=0
    liste=[]
    kume=set()
    for a in range(1,veri):
        for b in range(1,veri):
            for c in range(1,veri):
                # a, b ve c nin 1 den girilen degere kadar herbir sayı degeri icin dongü
                if a**2+b**2==c**2:
                    # pisagor sartının saglanma durumu
                    liste=[a,b,c]
                    # a,b ve c uclusunu listeyeatama
                    liste.sort()
                    # liste elemanlarını sıralama
                    kume.add((liste[0],liste[1],liste[2]))
                    # listenin uc elemenını kumeye atama(aynı eleman tekrarını onlemek icin)
    liste=list(kume)
    # kimeyi tekrar listeye donusturme sonuclar sıralı olması icin
    liste.sort()
    # liste elemanlarını sıralma
    for i in liste:
        # liste elemanlarını duzgun bir sırayla yazdırmak icin dongu
        sayac+=1
        print(i,end='  ')
        if sayac==5:
            # her 5 eleman yazdırma isleminden sonra alt satıra gecmek icin sayac
            print('')
            sayac=0

pisagor(100)


