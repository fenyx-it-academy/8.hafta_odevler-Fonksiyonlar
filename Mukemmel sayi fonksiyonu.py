"""1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın.
Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
Bir sayının, kendisi haric pozitif tam bolenleri toplami o sayiya esit ise mukemmel sayidir.
 Örnek olarak 28 mükemmel bir sayıdır (1+2+4+7+14=28)."""
def mukemmel_sayi(sayi):
    toplam=0
    for i in range(1,sayi):
        if sayi%i==0:
            toplam+=i
    if toplam==sayi:
        return "sayi mukemmeldir"
    return "sayi mukemmel degildir"
print(mukemmel_sayi(22))