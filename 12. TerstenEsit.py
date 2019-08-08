# Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız.
# örnek: madam, taco cat, utrecht sonuç: True, True, False

try:
    def tersiEsitMi(str):

        newStr = []
        index = len(str) - 1  # son indexe ulasmak icin uzunlugun 1 eksigini aldik
        while index >= 0:
            # stringin son elemanindan baslayarak tersten listeye aktariyoruz
            newStr.append(str[index])
            index -= 1

        tersStr = ''.join(newStr)  # liste elemanlarini join ile stringe cevirdik
        if str == tersStr:
            print(True)
        else:
            print(False)


    tersiEsitMi("kayak")
except:
    print('Hatali islem. Program sonlandirildi.. ')