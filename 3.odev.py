def mukemmelsayi():
    sayilar=[]
    for i in range(0,1001):
        liste=0
        bolunen = 1

        while True:
            if bolunen < i:  # girilen sayidan bir eksigine kadar bolme islemini yapar
                sonuc = i % bolunen
                if sonuc == 0:
                    liste+=bolunen
                    bolunen+=1
                    continue
                elif sonuc != 0:
                    bolunen+=1
                    continue
            else:
                if i==liste:
                    sayilar.append(i)
                    break
                else:
                    break
        if i <1001:
            continue
        else:
            break
    return print(sayilar)
mukemmelsayi()
