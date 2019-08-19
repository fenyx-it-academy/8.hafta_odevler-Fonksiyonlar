print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def dividings(a, b):
    tam1 = 0                                #bunlara burda cok luzum yok ama sus diye koyduk
    tam2 = 0
    exact_dividing1 = []
    exact_dividing2 = []
    lists = []
    for bolen in range(1, number1 + 1):         #+1 eklemedeki amac girilen sayiyida almasi range den kaynaklanan durum
        if(number1 % bolen) == 0:
            tam1 += 1                        #kac adet tam boleni vardir
            exact_dividing1.append(bolen)          #boleni listeye ekle
    for bolen in range(1, number2 + 1):         #+1 eklemedeki amac girilen sayiyida almasi range den kaynaklanan durum
        if (number2 % bolen) == 0:
            tam2 += 1                           # kac adet tam boleni vardir
            exact_dividing2.append(bolen)
            lists = [exact_dividing1, exact_dividing2]       #burasi asagida kullanmak icin yaptik
    return lists
# print(dividings())


def obeb(x, y):
    first_call = dividings(x, y)                  #onceki fonksiyondaki listeyi cagirmak icin
    ortaklar = []                               #iki listede ortak olanlari buraya aktar
    max_ortak = ""                              #hem ortak hem max olanlari buraya aktar
    for b in first_call[0]:                      #ilk listedeki tum elemanlari tara
        for a in first_call[1]:                  #ikinci listedeki elemanlari tara
            if a == b:                          #esit olan eleman varsa
                ortaklar.append(a)              #tanimlanan listeye ekle
                max_ortak = max(ortaklar)       #ortak elemanlarin enbuyugunu bul
    return max_ortak
# print(obeb(12,24))


while True:
    enter = input("Enter for continue 'C', enter for exit 'q': ").lower()
    if enter == 'q':
        print("Exiting...")
        break
    elif enter == "c":
        number1 = input("Enter first number: ")
        number2 = input("Enter second number: ")
        try:
            number1 = int(number1)
            number2 = int(number2)
            second_call = obeb(number1, number2)                   #fonksiyonumuzu cagiriyoruz istesek direkte yazabiliriz
            if number1 == 1 or number2 == 1:
                print("There is no dividing itself!")
            else:
                print(f"Numbers of {number1} and {number2} gcd(ebob) is: {second_call}")
        except ValueError:
            print("Please enter number..!")
    else:
        print("Please try again...")




#ALTERNATIF OBEB BULMA!!!!!!!!
# def obeb(sayi1,sayi2):
#
#     for i in range(int((sayi1+sayi2)/2),0,-1):
#         if sayi1%i == 0 and sayi2%i ==0:
#             break
#     return i
# print(obeb(12,24))
