def Asalsayiislemi(sayi):

    anahtar = True

    for i in range(2, sayi):    # 1 ve sayinin kendisini almayarak else olarak kullancaz
        if sayi % i == 0:
            anahtar = False
    return anahtar

while True:
    sayi = int(input("Kontrol Etmek IStediginiz Sayiyi Giriniz : \n"))

    if Asalsayiislemi(sayi):
        print(sayi, "Sayisi Asal Sayıdır")
    else:
        print(sayi, "Sayisi Asal Değildir")