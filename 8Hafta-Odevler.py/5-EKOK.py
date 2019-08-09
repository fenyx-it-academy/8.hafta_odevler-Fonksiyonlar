"EKOK Bulma"
def ekokbul(sayi1,sayi2):
    ekok = 1
    i = 2
    while True:
        if sayi1%i == 0 and  sayi2%i == 0 :
            ekok*=i
            sayi1//=i
            sayi2//=i
        elif sayi1%i == 0 and sayi2%i != 0:
            ekok*=i
            sayi1//=i
        elif sayi1%i != 0 and sayi2 %i == 0:
            ekok*=i
            sayi2//=i
        else:
            i+=1
        if (sayi1 == 1 and sayi2 == 1):

         return ekok
while True:
    sayi1 = int(input("birinci sayiy giriniz : "))
    sayi2 = int(input("ikinci sayiyi giriniz: "))
    print(ekokbul(sayi1,sayi2))
