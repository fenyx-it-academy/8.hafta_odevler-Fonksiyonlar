"""Bir sayinin tam bolenlerini bulan fonksiyon yaziniz"""

def tambolenleribulma(sayi):#ilk olarak bir fonksiyon yazdık
    tam_bolenler = []#tam bolenler icin bos bi liste olusturduk

    for i in range (2,sayi):#bu i degerlerlerinden herhangi biri bile bunu boluyorsa biz bunu listeye atmak istiyoruz

        if (sayi % i == 0):#sayiyi i ye bölüyoruz kalanı 0 ise bu sayiyi tam boluyordur
            tam_bolenler.append(i)
    return tam_bolenler

while True:

    sayi = input("Sayi: ")#ilk sayi aldık

    if (sayi=="q"):#programdan cıkılır
        print("Program Sonlandiriliyor")
        break

    else:
        sayi = int(sayi)

        print("Tam bolenler",tambolenleribulma(sayi))