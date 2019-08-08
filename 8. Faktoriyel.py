# Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.

def faktoriyel(sayi):
    faktoriyel = 1

    # sayi 1den buyuk ya da esit oldugu surece;
    while sayi >= 1:
        # faktoriyel degiskeni ile sayiyi carpip tekrar faktoriyele aktardik
        faktoriyel *= sayi
        sayi -= 1
    return faktoriyel


try:
    while True:
        sayi = input("Pozitif bir tamsayi girin: ")
        if sayi.isdigit() == True:
            # girilen deger eger rakamlardan olusuyorsa asagidaki islemler yapilir
            # input string oldugu icin inte cevirdik
            sayi = int(sayi)
            if sayi >= 0:  # sayinin pozitif olup olmadigina bakiyoruz
                print("{} sayisinin faktoriyeli: {}".format(sayi, faktoriyel(sayi)))
            else:
                print('Lutfen pozitif bir tamsayi girin!')
                continue
        else:
            print('Lutfen pozitif bir tamsayi girin!')
            continue
except:
    print('Hatali islem. Program sonlandirildi.. ')


