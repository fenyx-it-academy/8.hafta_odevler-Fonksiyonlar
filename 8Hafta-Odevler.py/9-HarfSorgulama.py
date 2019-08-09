"""Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf sayılarının veren bir fonksiyon yazınız."""

def sorgulamafonksiyon(s):
    lower =0#kucuk harfleri tutan degisken
    upper = 0#buyuk harfleri tutan degisken
    for c in s:#butun harflere tek tek bak
        if c.islower():#kucuk harf varsa kucuk harf degiskenine gonder
            lower+=len(c)
        if c.isupper():#buyuk harf varsa buyuk harf degiskenine gonder
            upper += len(c)
    print("kucuk harf sayisi:", lower, "buyukharf sayisi", upper)

while True:
    try:#string disinda bir degerde uyar
        s = input("bir sozcuk giriniz")

        print(sorgulamafonksiyon(s))
    except:
        print("bir hata olustu")