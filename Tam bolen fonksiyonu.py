"""Bir sayinin tam bolenlerini bulan fonksiyon yazınız."""

def tam_bolen(number):
    bolenler=[]
    for i in range(1,number):
        if number%i==0 :
             bolenler.append(i)

    return bolenler

print(tam_bolen(24))
