#Asal sayi olup olmadigini kontrol eden fonksiyon yazınız.

def asalmi(sayi):
    if(sayi==1):
        return False
    elif(sayi==2):
        return True
    else:
       for i in range(2,sayi):
           if(sayi%i==0):
               return False
       return True
 
while True:
    sayi=input("Sayi Giriniz:")
    if(sayi=="q"):
        print("Program Sonlandırıldı")
        break
    else:
        sayi=int(sayi)
        if(asalmi(sayi)):
            print(sayi,"Asal bir sayidir")
        else:
            print(sayi,"Asal sayi değildir")
