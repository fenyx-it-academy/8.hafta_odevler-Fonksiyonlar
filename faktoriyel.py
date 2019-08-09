#odev 8#
#Faktoriyel bulma#

def faktoriyel():
    sayi=int(input("Faktoriyelini almak istediginiz sayiyi giriniz: "))
    faktoriyel=1
    for i in range(1,sayi+1):
        faktoriyel*=i
    return faktoriyel
print("Girmis oldugunuz sayinin faktoriyeli: ",faktoriyel())
