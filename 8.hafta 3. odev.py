print('b.')
#>>>>>>>>>>>>>>>>...........mukemmel sayi...........<<<<<<<<<<<<<<<<<<<<<<<<<<<
'''
3. odev
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
  Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın. Bir sayının, 
  kendisi haric pozitif tam bolenleri toplami o sayiya esit ise mukemmel sayidir. 
  Örnek olarak 28 mükemmel bir sayıdır (1+2+4+7+14=28).
'''
def mukemmel_sayi():
    mukemmel_sayi = []              # mukemmel sayilari toplamak icin bos liste olusturduk
    for sayi in range(1, 1000):     # for range ile 1-1000 arasindaki sayilara baktik
        tam_bolenler_toplami = 0    # tam bolenleri toplamak icin basta toplami sifir olarak aldik
        for i in range(1, sayi):
            if sayi % i == 0:               # tam bolenlerine baktik
                tam_bolenler_toplami += i   # bolen sayilari topladik
        if tam_bolenler_toplami == sayi:    # if ile tam bolenleri toplami sayiya esit olanlari kont ettik
            mukemmel_sayi.append(sayi)      # esit olanlari listemize ekledik
    return f'1 ile 1000 arasindaki mukemmel sayilar : {mukemmel_sayi}'

print(mukemmel_sayi())