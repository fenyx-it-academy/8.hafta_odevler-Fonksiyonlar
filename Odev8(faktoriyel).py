##Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.
while True:
    def tamsayi(a):
        sonuc=1
        for i in range(1,a+1):
            sonuc *=i
        return "{} sayisinin faktoriyeli: {}".format(a,sonuc)
    sayi=input("Bir sayi giriniz cikis icin 'q' :").lower()
    if sayi=='q':
        break
    
    print(tamsayi(int(sayi)))
