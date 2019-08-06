#Bir sayinin tam bolenlerini bulan fonksiyon yazınız.
print("*** Sayinin Tam Bolenleri ***".center(30))
while True:
    def tam_bolen(a):
        liste=[]
        for i in range(1,a+1):
            if a%i==0:
                liste += [i]
        return liste
    sayi=input("Bir sayi giriniz cikis icin 'q':").lower()
    if sayi=='q':
        break
    print(tam_bolen(int(sayi)),"\n")
        
