print("Haydi Aklinizdaki Kelimeleri Alfabetik Olarak Siralayalim\n")
def sirala():
    kelime= input("Lutfen (-) ile ayirarak aklinizdan gecen kelimeleri
                  giriniz:")
    kelimeler=kelime.split("-")
    kelimeler.sort()
    print(*kelimeler,sep="-")

sirala()
