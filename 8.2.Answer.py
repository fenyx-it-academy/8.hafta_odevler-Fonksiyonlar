print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def isexact(*args):
    exact = []
    count = 0
    sequences = []                                   #referans olarak kullanacagimiz sayac veya listeleri burada gostermeliyiz. Daha sonra kodumuzda cagirabilelim
    if number == 0:
        return False
    else:
        for tam in range(2, number):
            if(number % tam == 0):
                exact.append(tam)                #yukarida tam bolen sayilardan liste olusturup bunun icine her boleni atiyoruz
                count += 1                          #kac adet tam bolen sayi vardir
                sequences = [count, exact]        #dizinleri burda liste seklinde tanittim kodumuzda cagiracagiz
        return sequences                             #return icindede gostermeliyiz


while True:
    number = input("Please input for exit 'q' or write a number for continue: ").lower()
    try:
        if number == "q":
            print("Exiting...")
            break
        else:
            number = int(number)
            call_function = isexact(number)
            if number == 1:
                print("There is no dividing itself!")
            elif isexact(number):
                adet = call_function[0]
                bolenler = call_function[1]
                print(f"There are(is) {adet} exact dividing for number of {number}. And number(s) is(are) {bolenler}.")
            else:
                print(f"There is no dividing 1 and itself for number of {number}!")
    except ValueError:
        print("Please enter a number..!")
