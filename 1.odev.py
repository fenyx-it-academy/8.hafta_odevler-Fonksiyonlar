def asalsayi():
    while True:
        try:
            numara = int(input("lutfen bir sayi giriniz\t:"))
            if numara < 2:
                print("girdiginiz sayi en az 2 olmalidir")
                continue
            if numara == 2:
                print("girdiginiz sayi asal sayidir")
                quit()
            bolunen = 2
            while bolunen < numara:  # girilen sayidan bir eksigine kadar bolme islemini yapar
                sonuc = numara % bolunen
                if sonuc == 0:
                    print("girdiginiz sayi asal sayi degildir")
                    quit()
                elif sonuc != 0:
                    k = numara - 1
                    if bolunen == k:  # bolunen sayi bolen sayidan bir eksigine kadar ulastimi kontrol eder
                        print("girdiginiz sayi asal sayidir")
                        quit()
                    else:
                        bolunen += 1
                        continue


        except ValueError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue
        except NameError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue

asalsayi()
