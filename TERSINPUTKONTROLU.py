"""Verilen inputların tersten de aynı olup olmadığını kontrol eden bir
 fonksiyon yazınız. örnek: madam, taco cat, utrecht sonuç: True, True, False"""

def fonk(*args):
    durum=" "
    for i in args:
        if i==i[::-1]:
            durum+="True"
        else:
            durum+="False"
        return durum

print(fonk("madam", "tacocat","utrecht"))