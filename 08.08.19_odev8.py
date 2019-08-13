def faktoryel ():                                                                       # fonksiyonumuzu adlandirdik
    sayi = input("Lutfen bir sayi giriniz : ")                                          # kullanicidan veri aldik

    if bool(sayi) == False:                                                             # hatali veri giris olasiligina karsilik kontrol koyduk
        print("Bos birakmayacak, bir sayi girecektin kardesim. Gecmis olsun !!!!")

    elif sayi == "0":                                                                   # hatali veri giris olasiligina karsilik kontrol koyduk
        print("0 sayi mi kardesim ???")

    else:                                                                               # dogru veri girisinde sonuca goturecek formulasyonu yaptik
        sayim = abs(int(sayi))

        faktoriyel = 1
        for i in range(1, sayim + 1):
            faktoriyel *= i
    return faktoriyel                                                                   # sonucu verdik


print(faktoryel())                                                                      # fonksiyonumuzu cgirdik