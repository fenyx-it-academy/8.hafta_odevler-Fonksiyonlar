print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

def capitalized(ikra):
    #letter = input("Lutfen kontrol etmek istediginiz bir yazi giriniz: ")
    big = 0
    small = 0
    for i in letter:
        if i.isupper():                                         #buyuk harf sorgula
            big += 1
        elif i.islower():                                       #kucuk harf sorgula
            small += 1
    liste = [big, small]                                        #asagida atif yapmak icin liste yaptik
    # print("Number of Big letter: ", big)
    # print("Number of Small letter: ", small)
    return liste

#capitalized()


while True:
    enter = input("Enter for continue 'C', enter for exit 'q': ").lower()
    if enter == 'q':
        print("Exiting...")
        break
    elif enter == "c":
        letter = input("Enter the text you want to get information: ")
        call = capitalized(letter)                                          #fonksiyondaki listeden atif yapmak icin kullanildi
        if not letter:                                                      #eger birsey girilmediyse uyar
            print("Please enter something!")
        else:
            print(f"There are {call[0]} big letter(s) and {call[1]} small letter(s) in the sentence.")   #fonksiyon cagrildi
    else:
        print("Please try again...")