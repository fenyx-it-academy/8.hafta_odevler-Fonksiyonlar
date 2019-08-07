print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def select():
    #words = input("Please write some words with between giving space: ")
    words2 = list(words.split(" "))                              #girilenleri bosluklardan ayirarak liste yaptik
    words3 = []                                                  #yeni bos liste tanimladik
    for i in words2:                                             #sade liste icinde dolansin
        if i not in words3:                                      #sade listede olupta yeni listede olmayan varsa
            words3.append(i)                                     #yeni listeye eklesin boylelikle tekrar olmamis olur
    return words3
#print(select())


while True:
    enter = input("Enter for continue 'C', enter for exit 'q': ").lower()
    if enter == 'q':
        print("Exiting...")
        break
    elif enter == "c":
        words = input("Please write some words with between giving space: ")
        if not words:                                                           #eger birsey girilmediyse uyar
            print("Please enter something!")
        else:
            print(f"Your new list without repeating is:\n{select()}")               #fonksiyon cagrildi
    else:
        print("Please try again...")
