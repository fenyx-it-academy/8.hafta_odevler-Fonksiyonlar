#odev 6#
#rakam olarak verilen sayinin harflerle yazilisi#

print("""harf olarak yazılmasını istediginiz sayiyi rakam olarak giriniz
En fazla iki basamaklı bir sayi girebilirsiniz\n""")
def oku():
    birler=[" ", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]
    onlar=["on","yirmi", "otuz", "kirk", "elli", "altmis", "yetmis", "seksen", "doksan"]
    sayi=input("cift basamakalı sayi giriniz: ")
    return  onlar[int(sayi[0])-1]+" " +  birler[int(sayi[1])]

print(oku())
