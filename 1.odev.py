'''
1-Asal sayi olup olmadigini kontrol eden fonksiyon yazınız.
'''

def asal_kontrol(a):
    kontrol = 0 # if bloğuna girip girmediğini kontrol amaçlı değişken tanımlıyorum

    for i in range(2,a):
        if a%i == 0:
            kontrol = 1 # değişkeni değiştirerek if bloğuna girip girmediğini kontrol ediyorum
            return print("Asal sayı değildir")

    if kontrol == 0:
        return print("Sayı asaldır")
asal_kontrol(229)


