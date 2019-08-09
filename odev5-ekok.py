def ekok(sayi1,sayi2):
    asalsayilar=[]
    sayac=0
    sayi=1
#for donguleri ile iki sayiyi tam bolen asal
#sayilari bulup ortak bi listeye yazdirdik

    for i in range(2,sayi1):
        if sayi1 % i == 0:
            sayac += 1

            if sayac != 0:
                asalsayilar.append(i)
    for i in range(2,sayi2):
        if sayi2%i==0:
            sayac+=1

            if sayac!=0:
                asalsayilar.append(i)
#daha sonra ortak listeye yazdirdigimiz butun sayilari
#for ile carpimini yaptik ve printle ekrana verdik
    for i in asalsayilar :
        sayi*=i
    print(sayi)

ekok(21,18)