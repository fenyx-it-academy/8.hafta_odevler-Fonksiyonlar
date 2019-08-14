##Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.
liste=[]
sayi=int(input("Bir sayi giriniz : "))


def faktoriyel():
    global liste
    for i in range(1,sayi+1):
        if i not in liste:
            liste += [str(i)]
    ##yukarida sayinin bilesenlerini liste haline getirdik.
    ##asagida *= yardimiyla bu bilesenleri birbiriyle carptik
    sayac=1
    adim=0
    for i in liste:
        if adim <= len(liste):
            sayac *=int(i)
            adim+=1
    print(sayac)
faktoriyel()              
