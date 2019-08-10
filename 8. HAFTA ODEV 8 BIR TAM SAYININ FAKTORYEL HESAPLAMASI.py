#POZITIF TAM SAYI FAKTORYEL HESAPLAMA FONKSIYONU
def faktoriyel(sayi):
    faktoriyel = 1

    while sayi >= 1:
        faktoriyel *= sayi
        sayi -= 1
    return faktoriyel


try:
    while True:
        sayi = input("Pozitif bir tamsayi girin: ")
        if sayi.isdigit() == True:
            sayi = int(sayi)
            if sayi >= 0:  
                print("{} sayisinin faktoriyeli: {}".format(sayi, faktoriyel(sayi)))
            else:
                print('Lutfen pozitif bir tamsayi girin!')
                continue
        else:
            print('Lutfen pozitif bir tamsayi girin!')
            continue
except:
    print('Hatali islem. Program sonlandirildi.. ')
