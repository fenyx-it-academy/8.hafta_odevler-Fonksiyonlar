print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

def faktorial(number):
    faktor = 1
    for i in range(1, number+1):
        faktor *= i
    return faktor

# print(faktorial(5))


while True:
    enter = input("Enter for continue 'C', enter for exit 'q': ").lower()
    if enter == 'q':
        print("Exiting...")
        break
    elif enter == "c":
        number = int(input("Enter number as you want to learn factorial: "))
        try:
            print(f"Number of {number} factorial is {faktorial(number)}. ")                #fonksiyon cagrildi
        except KeyError:
            print("Error! please enter number...")
    else:
        print("Please try again...")