print('b.')
'''1- Asal sayi olup olmadigini kontrol eden fonksiyon yazınız.'''

def asal_sayi(sayi):
    for i in range(2,sayi+1):
        if sayi%i==0:           # girilen sayiyi bolen bir sayi olup olmadigini kontrol ediyoruz
            return f"{sayi} : asal bir sayi degil"
        return f"{sayi} : asal bir sayi"
try:                                # sayi olup olmadigini kontrol ediyoruz
    sayi=int(input('2 den buyuk bir sayi giriniz....:'))
    if sayi>2:          # 2 den buyuk olmasini kontrol ettik
        print(asal_sayi(sayi))      # fonksiyonumuzu cagiriyoruz
    else:
        print('\nlutfen....2 den buyuk bir sayi giriniz')
except ValueError:
    print('lutfen sayi giriniz')