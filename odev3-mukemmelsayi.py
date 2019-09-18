def mukemmel(sayi=1000):
    mukmmel=[]
#range ile sayimiza kadar olan butun
#sayilari tek tek alip bu sayilarin
#1 den kendisine kadar olan butun
#sayilara bolduk ve kendisini
#tam bolen sayilari listemize yazdirdik
    for i in range(2,sayi+1):
        sayilar = []
        for z in range(1,i):
            if i%z==0:
                sayilar.append(z)
        if i==sum(sayilar):
            mukmmel.append(i)
#listeye yazdigimiz butun sayilari sum ile toplayarak
#kendisine esit olup olmama durumuna baktik
#eger esitse mukemmel sayi demek icin farkli bir listeye
#aldik
    for i in mukmmel:
        print(f'{i} sayisi mukemmel sayidir.')

mukemmel()