def ekok(sayi1,sayi2):
    sayilar=[]
    sayilar1=[]
    ekok=[]
#for dongusu ile iki sayi icinde o sayiya kadar
#olan butun sayilarla diger sayiyi carptik
#boylelikle her ikisinin ortak katlarini
#bulmus olduk bunu yazdigimiz listenin
#en kucuk elemani ekok u vermis oluyor
    for i in range(1,sayi1+1):
        sayi=sayi2*i
        sayilar.append(sayi)
    for i in range(1,sayi2+1):
        sayi=sayi1*i
        sayilar1.append(sayi)
    for i in sayilar:
        if i in sayilar1:
            ekok.append(i)
    print(min(ekok))
ekok(21,552)
