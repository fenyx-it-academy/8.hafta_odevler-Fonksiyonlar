#odev 9#
#buyuk-kucuk harf sayısı hesaplama#

def sayi():
    buyuk=0
    kucuk=0
    kelime=input("Lutfen buyuk/kucuk harf iceren bir kelime giriniz: ")
    for i in kelime:
       if  i.islower()==True:
           kucuk+=1
       elif i.isupper()==True:
           buyuk+=1
    son="buyuk harf sayisi:"+str(buyuk)+"\n"+"kucuk harf sayisi:"+str(kucuk)
    return son

print(sayi())
