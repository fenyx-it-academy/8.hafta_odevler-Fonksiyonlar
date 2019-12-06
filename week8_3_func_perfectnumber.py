def perfectnum(num):
    sum= 0
    for i in range(1, num):
        if (num % i == 0):
            sum += i
    if (num == sum):
        return True
perfectnumbers = []

for i in range(1, 1000):
    if (perfectnum(i)):
        perfectnumbers.append(i)  # listeye ekledik.

print("Perfect Numbers Between 1 and 1000 are\n", perfectnumbers)