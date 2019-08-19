print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

units_digit = {"1": "bir ", "2": "iki ", "3": "uc ", "4": "dort ", "5": "bes ", "6": "alti ", "7": "yedi ",
               "8": "sekiz ", "9": "dokuz ", "0": ""}
tens_digit = {"1": "on ", "2": "yirmi ", "3": "otuz ", "4": "kirk ", "5": "elli ", "6": "altmis ", "7": "yetmis ",
         "8": "seksen ", "9": "doksan ", "0": ""}


def trans_numbers(*args):
    #number = input("sayi girniz: ")
    return tens_digit[number[0]].capitalize() + units_digit[number[1]]      #girilen sayinin 1. ve 2. karakterini alip yukardaki sozlukte karsiligini gir dedik
                                                                            #ilk girilen sayinin turkce karsiliginin ilk harfi capitalize ile buyuk yapildi
#trans_numbers()


while True:
    enter = input("Enter for continue 'C', enter for exit 'q': ").lower()
    if enter == 'q':
        print("Exiting...")
        break
    elif enter == "c":
        number = input("Enter number as you want to translate: ")
        try:
            print("Entering number with writing: ", trans_numbers())                #fonksiyon cagrildi
        except (KeyError, IndexError):
            print("Error! please enter number...")
    else:
        print("Please try again...")