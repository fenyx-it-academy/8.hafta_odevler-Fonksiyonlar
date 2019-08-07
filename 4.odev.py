def EBOB():
    while True:
        try:
            numara1= int(input("lutfen ilk sayiyi giriniz\t:"))
            numara2=int(input("Lutfen ikinci sayiyi giriniz\t:"))
        except ValueError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue
        except NameError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue

        if numara1 < 2 or numara2 < 2:
            print("girdiginiz sayi en az 1 olmalidir")
            continue
        liste1=[]
        liste2=[]
        bolunen = 2

        while True:
            if bolunen <= numara1:  # girilen sayidan bir eksigine kadar bolme islemini yapar
                sonuc = numara1 % bolunen
                if sonuc == 0:
                    liste1.append(bolunen)
                    bolunen+=1
                    continue
                elif sonuc != 0:
                    bolunen+=1
                    continue
            else:
                break
        bolunen1=2
        while True:
            if bolunen1 <= numara2:  # girilen sayidan bir eksigine kadar bolme islemini yapar
                sonuc = numara2 % bolunen1
                if sonuc == 0:
                    liste2.append(bolunen1)
                    bolunen1 += 1
                    continue
                elif sonuc != 0:
                    bolunen1 += 1
                    continue
            else:
                break
        liste3=set(liste1)
        liste4=set(liste2)
        if liste3.isdisjoint(liste4)==True:
            print("Girilen iki sayinin EBOB degeri yoktur")
            quit()
        else:
            liste5=liste3.intersection(liste4)
            liste6=list(liste5)
            liste6.sort()
            uzunluk=len(liste6)
            print("girmis oldugunuz iki sayinin EBOB={}".format(liste6[uzunluk-1]))
            quit()

EBOB()