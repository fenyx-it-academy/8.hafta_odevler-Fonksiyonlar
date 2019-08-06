#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
#Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
#Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)
def mukemmel(a):
    liste=[]
    for i in range(1,a):
        if a%i==0:
            liste +=[i]
    return sum(liste)
mukemmel_sayilar=[]
for sayi in range(1,1000):
    if mukemmel(sayi)==sayi:
        mukemmel_sayilar += [sayi]
print(mukemmel_sayilar)
        
        
    

    
    

