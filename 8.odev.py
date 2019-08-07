def faktoriyel():
    while True:
        try:
            sayi= int(input("lutfen sayiyi giriniz\t:"))
        except ValueError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue

        if sayi < 1:
            print("girdiginiz sayi en az 1 olmalidir")
            continue
        liste=[i for i in range(1,sayi+1)]
        deger=1
        for i in range(liste[0],liste[len(liste)-1]):

            deger=deger*i
        return deger*len(liste)

print(faktoriyel())