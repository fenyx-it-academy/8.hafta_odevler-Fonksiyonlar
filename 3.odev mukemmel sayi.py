##1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
##Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
##Bir sayının, kendisi haric pozitif tam bolenleri toplami o sayiya esit ise
##mukemmel sayidir. Örnek olarak 28 mükemmel bir sayıdır (1+2+4+7+14=28).

def mukemmel_sayi(sayi):
    while sayi>1:
        sayi -= 1
        toplam=0
        bolunebilenler = []
        mukemmel_sayi= []
        for i in range(1,sayi):
            if(sayi%i == 0):
                bolunebilenler += [str(i)]
                toplam +=int(i)    
        if (sayi == toplam):
            mukemmel_sayi += [str(i+1)]
            print(*mukemmel_sayi, "sayisi mukemmel sayidir")    

mukemmel_sayi(int(input("Bir sayi giriniz : ")))      
















