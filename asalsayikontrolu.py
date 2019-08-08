

def asal_mi(sayi): #ilk fonksiyonu yazdık
    if (sayi ==1): #sayimiz asalsa fonksiyon true degerini döndürecek
        return False

    elif (sayi==2):#sayimiz eger 2 ise
        return True#bu degeri göster

    else:
        for i in range(2,sayi):#buradaki herhangi bir sayi i degerini bölüyorsa true
            if (sayi % i == 0):
                return False
            return True

while True:
    sayi = input("Sayi : ")#ilk basta sayiyi aldık

    if (sayi =="q"):#programdan cikilmak istendiginde
        break

    else:
        sayi=int(sayi)#veri tipi dönüstürmesi yaptık

        if (asal_mi(sayi)): #sayinin asal mi degil mi kontrolu icin olusturuldu
            print(sayi,"asal bir sayidir. ")

        else:
            print(sayi,"asal bir sayi degildir.")