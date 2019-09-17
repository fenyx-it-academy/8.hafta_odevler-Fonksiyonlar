def asal_sayı():
    değer=0
    sayi=input("sayı giriniz:")
    for i in range(2,int(sayi)):
        if(int(sayi)%i==0):
            değer+=1
            break
    if(değer!=0):
        print(sayi,"Sayısı Asal Değildir.")
    else:
        print(sayi,"Sayısı Asal sayıdır.")
asal_sayı()
