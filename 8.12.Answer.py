print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def palindrome():
    #letter = input("Lutfen Herhangi bir kelime giriniz: ")
    for i in letter:
        for k in letter[-1]:
            if i != k:
                #print("Girdiginiz kelimenin tersten okunusu ayni degil")
                return False
            else:
                #print(letter, "kelimesinin terseten okunusu aynidir")
                return True
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