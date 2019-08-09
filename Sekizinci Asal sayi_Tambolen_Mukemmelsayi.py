
print("Prime number inquiry")
def asalmi(x):
    try:
        if (int(sayi) > 0):
            for i in range(2, int(sayi)):
                if int(sayi) % i == 0:
                    print("Not Prime Number")
                    break
            else:
                print("Congrats!!! {} is Prime Number...".format(sayi))
                return x
        else:
            print("Enter a positive number!")
    except ValueError:
        print("You can enter only (+)positive numbers...")

while True:
    sayi = input("Enter number to seek: ")
    if asalmi(sayi):
        break
    else:
        continue



##############################################################################

print("Bir Sayinin Tum Tam Sayi Bolenlerini Bulma")
def tamsayibolen():
    bolenler=[]
    try:
        sayi = int(input("Sorgulamak istediginiz sayiyi giriniz:"))
        for i in range(1,(sayi+1)):
            if sayi%i==0:
                bolenler.append(i)
            else:
                continue
        return print(bolenler)
    except ValueError:
        print("Lutfen sayisal bir deger giriniz.")
tamsayibolen()

################################################################
print("Mukemmel Sayi Bulmaca")
def mukemmelmi():
    while True:
        bolenler = []
        try:
            sayi = int(input("Sorgulamak istediginiz sayiyi giriniz:"))
            for i in range(1, sayi):
                if sayi % i == 0:
                    bolenler.append(i)
                else:
                    continue
            print(sayi,"sayisisnin tam bolenlerinin toplami",sum(bolenler),"dir.")
            if sum(bolenler)==sayi:
                return print(sayi,"Mukemmel bir sayidir.")
            else:
                print(sayi,"Mukemmel degil, Ama zaten mukemmelik nadir bulunan bir ozelliktir.")
        except ValueError:
            print("Lutfen sayisal bir deger giriniz.")
mukemmelmi()

