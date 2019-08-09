def tambolen(sayi):
    sayilar=[]
#aldigimiz sayiyi range ile kendisine kadar olan butun sayilara
#bolduk ve kalanin 0 oldugu durumlarda bunu listeye ekledik
#ve bunu yazdirdik
    for i in range(2,sayi) :
        if sayi%i==0:
            sayilar.append(i)
    print(f'{sayi} sayisini tam bolen sayilar {sayilar}')
tambolen(24)