def sayikontrol():
    while True:
        try:
            sayi= int(input("lutfen iki basamakli bir sayi giriniz\t:"))
        except ValueError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue
        except NameError:
            print("Lutfen girdiginiz degeri kontrol ediniz")
            continue
        if sayi<0:
            print("Girdiginiz sayi pozitif olmalidir")
            continue
        sayi=str(sayi)
        if len(sayi) < 2 or len(sayi) > 2:
            print("girdiginiz sayi iki basamakli olmalidir")
            continue
        birlerbasamagi={"0":"","1":"bir","2":"iki","3":"uc","4":"dort","5":"bes",
                        "6":"alti","7":"yedi","8":"sekiz","9":"dokuz"}
        onlarbasamagi = {"0": "", "1": "on", "2": "yirmi", "3": "otuz", "4": "kirk", "5": "elli",
                          "6": "altmis", "7": "yetmis","8": "seksen", "9": "doksan"}
        sayi=list(sayi)
        birler=birlerbasamagi.get(sayi[1])
        onlar=onlarbasamagi.get(sayi[0])
        return onlar+" "+birler

print(sayikontrol())