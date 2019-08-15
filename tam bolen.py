#odev 2#
#bir sayının tam bolenlerını bulma#

print("""Tam bölenlerini bulmak istediginz sayiyi giriniz.
Tam bolen sayılar liste olarak ekrana gelecektir.\n""")
def tambul(a):
    list=[]
    for i in range(1,a):
        if a%i == 0:
            list.append(i)
    return list
print(tambul(int(input("Tam bolenlerini bulmak istediginiz sayiyi giriniz:  "))))
