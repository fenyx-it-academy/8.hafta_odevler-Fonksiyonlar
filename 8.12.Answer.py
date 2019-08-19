print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def palindrome():
    liste = []                                                      #kelimeleri bu listeye eklicez
    letters = letter.split(" ")                                     #bosluklardan bolerek liste olustursun
    for i in letters:
        empty_letter = ""                                           #bos string tanimlayalim icine kelimeleri str olarak atsin
        for k in range(len(i)-1, -1, -1):                           #ayrilan herbir kelime sayisindan bir eksigiyle baslayip sondaki kelimeye kadar tersten tarasin
            empty_letter += i[k]                                    #herbir taranan kelime string olarak eklensin
        if empty_letter != i:
            #print("Girdiginiz kelimenin tersten okunusu ayni degil")
            liste.append(False)
        else:
            #print(letter, "kelimesinin terseten okunusu aynidir")
            liste.append(True)

    return liste
#palindrome()


while True:
    enter = input("Enter for continue 'C', enter for exit 'q': ").lower()
    if enter == 'q':
        print("Exiting...")
        break
    elif enter == "c":
        letter = input("Please write some words: ")
        if not letter:                                               #eger birsey girilmediyse uyar
            print("Please enter something!")
        else:
            print(palindrome())                                      #fonksiyon cagrildi. cikti olarak yukarda tanimlanan sekilde ya True yada False verecek
    else:
        print("Please try again...")
