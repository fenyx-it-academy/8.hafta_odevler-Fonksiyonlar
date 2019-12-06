# 4. Kullanıcıdan 2 tane sayı alarak bu sayıların
# en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

# ebob  =  greatest common divisor
def gcd(a, b):
    if (a > b):
        smallnumber = b
    else:
        smallnumber = a

    c = smallnumber

    while (c > 0):
        if (a % 1 == 0 and b % c == 0):
            return c
        c -= 1
    return 1


while True:
    a = int(input("Enter first number:.\n"))
    b = int(input("Enter second number:.\n"))
    d = gcd(a, b)

    print("Greatest Common Divisor of\n{} and {} is -> {}".format(a,b,gcd(a,b)),"\n")
