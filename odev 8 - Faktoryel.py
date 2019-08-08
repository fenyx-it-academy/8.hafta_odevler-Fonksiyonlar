number = int(input("Please enter a number :"))

def faktor(number):
    if number==0:
        return 1
    else:
        b=1
        for a in range(1,number+1):
            b *=a
        return b
print(faktor(number))