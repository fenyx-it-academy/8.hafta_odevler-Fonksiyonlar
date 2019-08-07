print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def to_sort():
    #letter = input("Please write some words with between add (-) symbol: ")
    sequence = []                                   #bos liste olustur
    sequence = letter.split("-")                    #girilen yazidaki kelimeleri - den ayirarak listeye atar
    sequence.sort()                                 #siralama yap
    print("Sorted the text is:")
    return print(*sequence, sep="-")                #siralama yapilan listedeki kelimeler arasina tekrar - koyar


#to_sort()


while True:
    enter = input("Enter for continue 'C', enter for exit 'q': ").lower()
    if enter == 'q':
        print("Exiting...")
        break
    elif enter == "c":
        letter = input("Please write some words with between add (-) symbol: ")
        if not letter:                                                      #eger birsey girilmediyse uyar
            print("Please enter something!")
        else:
            to_sort()                                                       #fonksiyon cagrildi
    else:
        print("Please try again...")