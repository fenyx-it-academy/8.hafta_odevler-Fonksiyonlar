print('b.')

'''2-Bir sayinin tam bolenlerini bulan fonksiyon yazınız.'''

def tam_bolenler(sayi):
    tam_bolenler=[]                     # tam bolen sayilari toplamak icin bos bir liste olusturduk
    for bolen in range(1, sayi + 1):    # for range ile girilen sayiya kadar olan sayilari bulduk
        if sayi % bolen == 0:           # if ile bolen sayilari kontrol ettik
            tam_bolenler.append(bolen)  #bolen sayilari listemize ekledik
    return f'{sayi} nin tam bolenleri :{tam_bolenler}'
try:                                    # try except ile sayi girilmesini kontrol ettik
    sayi = int(input('bir sayi gir...:'))
    print(tam_bolenler(sayi))           #  fonk cagiriyoruz
except ValueError:
    print('\nlutfen sayi giriniz')
