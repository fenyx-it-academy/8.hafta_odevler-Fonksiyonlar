# Verilen inputların tersten de aynı olup olmadığını
# kontrol eden bir fonksiyon yazınız.
# örnek: madam, taco cat, utrecht
# sonuç: True, True, False
import time


def rev_reader(*args):
    list = " "
    for i in args:
        if i == i[::-1]:
            list += "True"
        else:
            list += "False"
        return list

print("Type A Word & Check, \nIf It Is Reverse Readable")
while True:
    a = input("*Enter a word, q--»exit: ")
    if a == "q":
        print("Görüşmek üzere, prg sonlandırılıyor!")
        time.sleep(1)
        break
    else:
        print("-",a,"--»",rev_reader(a))
