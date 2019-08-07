def bolunensayi():
    while True:
        try:
            numara = int(input("lutfen bir sayi giriniz\t:"))
        except ValueError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue
        except NameError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue

        if numara < 1:
            print("girdiginiz sayi en az 1 olmalidir")
            continue
        liste=[]
        bolunen = 1

        while True:
            if bolunen < numara:  # girilen sayidan bir eksigine kadar bolme islemini yapar
                sonuc = numara % bolunen
                if sonuc == 0:
                    liste.append(bolunen)

                    bolunen+=1
                    continue
                elif sonuc != 0:
                    bolunen+=1
                    continue
            else:
                return liste






print(bolunensayi())