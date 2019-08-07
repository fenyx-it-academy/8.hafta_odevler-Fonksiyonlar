def faktoriyel(sayi=int(input('faktoriyel sayisi:'))):
    carpim=1
    for i in range(-sayi,0): #burada geriye dogru saydirma yapildi
        carpim*=abs(i)       #i degerlerinin de mutlak degerleri ile carpildi
    return carpim
#-----------------------------------------------------

print(faktoriyel())
#-----------------------------------------------------
def faktoriyel_2(sayi_2=int(input('faktoriyel sayisi:'))):

    cikar=sayi_2
    carp=1
    for i in range(sayi_2):#burada sayi degeri kadar range yapildi

        carp*=cikar       #sayi degeri 1 eksiltilerek carpildi
        cikar-=1
    print('{} sayisinin faktoriyeli {}'.format(sayi_2,carp))
#------------------------------------------------------
faktoriyel_2()
