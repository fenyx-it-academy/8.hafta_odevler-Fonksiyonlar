def read ():                                                        # fonksiyonumuzu adlandirdik
    rakamlar = {
        "1": "bir",
        "2": "iki",
        "3": "uc",
        "4": "dort",
        "5": "bes",
        "6": "alti",
        "7": "yedi",
        "8": "sekiz",
        "9": "dokuz",
    }
                                                                    # 2 ayri sozluk olusturduk
    onlar = {
        "1": "on",
        "2": "yirmi",
        "3": "otuz",
        "4": "kirk",
        "5": "elli",
        "6": "altmis",
        "7": "yetmis",
        "8": "seksen",
        "9": "doksan",
    }

    sayi = input("Lutfen 2 basamakli bir sayi giriniz : ")          # kullanicidan sayi aldik

    if bool(sayi) == False:                                         # hatali giris olasiligina karsi kontrol olusturduk
        print("Bos birakmayacak, 2 basamakli sayi girecektin kardesim. Gecmis olsun !!!!")

    elif len(sayi) < 2 or len(sayi) > 2:                            # hatali giris olasiligina karsi kontrol olusturduk
        print("2 basamakli bir sayi girmeyi beceremedigin icin yallah !!!!")

    elif len(sayi) == 2:                                            # sonuca goturecek formulasyonu yazdik
        sayim_list = list(sayi)

        onlarim = onlar[sayim_list[0]]
        birlerim = rakamlar[sayim_list[1]]
        print(onlarim, birlerim)
        quit()

print(read())                                                       # fonksiyonumuzu cagirdik