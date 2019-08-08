"""Kullanıcıdan bir input alan ve bu inputun içindeki büyük
 ve küçük harf sayılarının veren bir fonksiyon yazınız."""

def kucukbuyuk():
    giris= input("Giris yapiniz: ")
    buyuk = 0
    kucuk = 0

    for i in giris:
        if i.isupper():
            buyuk+=1

        elif i.islower():
            kucuk+=1
    return kucuk,buyuk
print("Küçük Büyük Harf: ", kucukbuyuk())

