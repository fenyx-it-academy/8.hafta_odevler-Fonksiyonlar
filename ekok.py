#odev 4#
#ekok bulma#

print("""İki sayi giriniz
Ekokunu size verelim\n""")
def ebob(sayi1,sayi2):
    list=[]
    for i in range(1,sayi2+1):
        if sayi1%i==0 and  sayi2%i==0:
            list.append(i)
            a=max(list)
    return a

def okek():
    sayi1=int(input("1.sayi: "))
    sayi2=int(input("2.sayi: "))
    okek=(sayi1*sayi2)/ebob(sayi1,sayi2)
    print("sayıların okeki: ",okek)
    return okek
okek()
