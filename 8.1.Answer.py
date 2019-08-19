print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def prime(*args):
    if number == 1 or number == 0:                             #false asal degildir
        return False
    elif number == 2:                           #true asaldir
        return True
    else:
        for bolen in range(2, number//2 + 1):               #1 haric sayiya kadar olan kismin bolumunden kalan sifir bir sayi varsa
            if number % bolen == 0:
                return False                                #asal sayi olmadigi durumda return False donsun
        return True                                         #aksi durumda return true yani asal sayidir


while True:
    number = input("Please input for exit 'q' or write a number for continue: ").lower()
    try:
        if number == "q":
            print("Exiting...")
            break
        else:
            number = int(number)
            if prime(number):                               #prime() fonksiyonunu cagiriyoruz asallik kontrolu icin. ASAL ISE
                print(f"{number} is prime number.")
            else:
                print(f"{number} is not prime number!")       #asal degilse
    except ValueError:
        print("Please enter a number...")


