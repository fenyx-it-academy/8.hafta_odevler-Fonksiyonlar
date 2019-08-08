
def divider(number):            # girilen argumanin tam bolen listesini veren fonksiyon
    int_number = []
    for i in range(1,number+1):
        if number % i == 0:
            int_number += [i]
    return int_number

a = int(input("please enter first number :"))
b = int(input("please enter second number :"))

def obeb(a,b):
    """ girilen iki parametrenin OBEB ini bulan fonksiyon """
    c = list(set(divider(a)).intersection(set(divider(b))))  # ilk sayinin ve ikinci sayinin tam bolenlerini kumeye donusturup kesisimini listeye donustur
    c = max(c)                                              # bu listenin maksimumunu bul, bu iki sayinin obebidir.
    return c
print(obeb(a,b))