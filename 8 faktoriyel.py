def faktoriyel(numara):
    faktoriyell = 1
    for i in range(1, numara + 1):
        faktoriyell *= i
    print("Fatoriyel : ", faktoriyell)

sayi = int(input("Faktoriyeli Hesablanacak Sayıyı Giriniz : "))
faktoriyel(sayi)


