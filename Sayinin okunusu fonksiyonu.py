"""
 Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
 Örnek: 97 ---------> Doksan Yedi
"""

def okunus():
    birler_basamagi=[" ", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"]
    onlar_basamagi=["on","yirmi", "otuz", "kirk", "elli", "altmis", "yetmis", "seksen", "doksan"]
    sayi=input("sayiyi giriniz:")
    return  onlar_basamagi[int(sayi[0])-1]+" " +  birler_basamagi[int(sayi[1])]

print(okunus())