#odev 4#
#ebob bulma#

print("""İki sayi giriniz
Ebobunu size verelim\n""")
def ebob():
    sayi1=int(input("1.sayi: "))
    sayi2=int(input("2.sayi: "))
    list=[]
    for i in range(1,sayi2+1):
        if sayi1%i==0 and  sayi2%i==0:
            list.append(i)
            a=max(list)
    return a

print(ebob())
