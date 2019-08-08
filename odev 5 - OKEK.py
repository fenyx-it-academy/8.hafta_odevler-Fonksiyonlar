def divider(number):            # girilen argumanin tam bolen listesini veren fonksiyon
    int_number = []
    for i in range(1,number+1):
        if number % i == 0:
            int_number += [i]
    return int_number

a = int(input("please enter first number :"))
b = int(input("please enter second number :"))

def obeb(a,b):                  # alinan iki parametrenin OBEB ini bulan fonksiyon
    c = list(set(divider(a)).intersection(set(divider(b))))
    c = max(c)
    return c

def okek(a,b):
    """iki sayinin OKEK ini bulan fonksiyon"""
    return (a*b)/obeb(a,b)

print(okek(a,b))

