#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
# Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
# Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

def mukemmel_sayi(sayi):
    goster=[]

    for i in range(sayi):
        for don in range(1,i):#sifir hatasini onlemek icin
            if i % don ==0: #pozitif bolenleri buluyoruz listeye atiyoruz
                goster+=[don]


        if i==sum(goster): #eger pozitif bolenlerin toplami sayiya esitse mukemmel sayiyi buluyoruz
                print(*goster,'=',sum(goster))
                goster=[]

        else:           #degilse listeyi bosaltip diger sayiyi kontrol ediyoruz
            goster = []



mukemmel_sayi(1000)
