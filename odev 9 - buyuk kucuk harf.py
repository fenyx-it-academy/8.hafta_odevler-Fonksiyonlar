kelime = input("Bir yazi giriniz :")

def harf(kelime):
    kucuk=0
    buyuk=0
    for i in kelime:

        if i.islower()==True:
            kucuk+=1

        elif i.isupper()==True:
            buyuk+=1
    print(""" "{}" yazisindaki
                    Buyuk Harf Sayisi : {}
                    Kucuk Harf Sayisi : {}""".format(kelime,buyuk,kucuk))

harf(kelime)