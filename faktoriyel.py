print("Factoriyel Number Calculate Programme")

def faktoriyel(x):
    while True:
        try:
            faktoriyell=1
            sayi=int(input("Please enter the number to calculate:"))
            if sayi<0:
                raise ValueError("Please enter positive number.")
            for i in range(1,sayi+1):
                faktoriyell*=i
            return print(faktoriyell)
        except ValueError:
            print("Please enter positive number.")
faktoriyel(1)
