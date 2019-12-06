#5. Kullanıcıdan 2 tane sayı alarak bu sayıların
#en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

# ekok  =  Least common multiple (LCM)
def lcm(a,b):
    if (a > b):
        bignumber = b
    else:
        bignumber = a

    c = bignumber

    while (c <a*b):
        if (c % a == 0 and c % b == 0):
            return c
        c += 1
    return (a*b)


while True:
    a = int(input("Enter first number:.\n"))
    b = int(input("Enter second number:.\n"))
    d = lcm (a, b)

    print("Least Common Multiple of\n{} and {} is -> {}".format(a,b,lcm(a,b)),"\n")
