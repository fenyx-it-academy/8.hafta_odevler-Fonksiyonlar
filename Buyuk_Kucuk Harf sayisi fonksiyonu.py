"""
9. Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf sayılarının veren bir fonksiyon yazınız.
"""
def buyuk_kucuk_harf():
    buyuk=0
    kucuk=0
    kelime=input("Lutfen buyuk/kucuk harf iceren bir kelime giriniz:")
    for i in kelime:
       if  i.islower()==True:
           kucuk+=1
       elif i.isupper()==True:
           buyuk+=1
    sonuc="buyuk harf sayisi:"+str(buyuk)+"kucuk harf sayisi:"+str(kucuk)
    return sonuc

print(buyuk_kucuk_harf())
