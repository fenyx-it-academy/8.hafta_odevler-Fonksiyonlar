#Asal sayi olup olmadigini kontrol eden fonksiyon yazınız.
print("*** Asal sayi mi? ***".center(30))
while True:
    def asal_sayi(a):
        if a==0 or a==1 or a<0:
            return "Lutfen ikiden buyuk pozitif sayi giriniz."
        for i in range(2,a):
            if (a%i)==0:
                return a, "bir asal sayi degildir."
        return a,"bir asal sayidir."
    sayi=input("Bir sayi giriniz cikis icin 'q':").lower()
    if sayi=='q':
        break
    
    print(asal_sayi(int(sayi)),"\n")
    
    
