# Kullanıcıdan bir input alin ve bu inputun içindeki büyük ve küçük harf sayılarını veren bir fonksiyon yazınız.
print(""""
Buyuk ve Kucuk Harfleri Bulma Fonksiyonu

cikis icin 'q' ya basin..
""")
import string

def buyukKucukHarf(str):
    kucukHarfler = []
    buyukHarfler = []
    k = 0 #kucuk harf adedi
    b = 0 #buyuk harf adedi

    for i in str:
        if i in string.ascii_lowercase:
            #kucuk harfleri bulup listeye aktardik
            kucukHarfler.append(i)
            k+=1 #kucuk harf adedini artirdik
        elif i in string.ascii_uppercase:
            # buyuk harfleri bulup listeye aktardik
            buyukHarfler.append(i)
            b+=1 #buyuk harf adedini artirdik

    print('{} adet kucuk harf vardir. Kucuk harfler {}'.format(k, kucukHarfler))
    print('{} adet buyuk harf vardir. Buyuk harfler {}'.format(b, buyukHarfler))

try:

    while True:
        str = input('Bir string girin: ')
        buyukKucukHarf(str)
except:
    print('Hatali islem. Program sonlandirildi.. ')