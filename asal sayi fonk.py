def asal(sayi=int(input('sayi giriniz'))):

    if sayi==0 or sayi==1:
        print(sayi,'asal degildir')#sayiyi kendinden onceki sayilara boleriz
    for tur in range(2,sayi):#eger pozitif bir boleni varsa asal degildir
        if sayi % tur==0:
            print(sayi,' asal sayi degildir')
            break
        else:
            print (sayi,' asal sayidir ' )# pozitif bolen yoksa asaldir
            break


asal()
