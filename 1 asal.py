#ASAL SAYI
def Asal (sayi,adet):
    for i in range(2,sayi+1):
        if sayi%i==0:
            adet+=1
    if adet==1:
        print ("asaldir")
    else:
        print ("asal degildir")

sayi=input("sayi giriniz:")
adet=0
Asal(sayi,adet)