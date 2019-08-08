# ---------------------------------8. HAFTA ODEVLER - FONKSIYONLAR---------------------------------

# -------------1. ODEV - Asal Sayi mi?-------------
def isPrimeNumber(number):
    isTrue = True
    # Only numbers greater than 1 can be prime numbers
    if number > 1:
        while isTrue:
            # See if the number is divisible by any other number than 1 and itself
            for i in range(2, number//2+1):
                if number % i == 0:
                    print("\n{} is not a prime number.".format(number))
                    isTrue = False
                    break
                elif i == 15:
                    isTrue = False
            # If this else block is executed, that means any condition above is not met
            # so the number is a prime number
            else:
                print("\n","\u2605" * 3 + "{} is a prime number!".format(number) + "\u2605" * 3, sep='')
                isTrue = True
                break
    else:
        print("\n{} is not a prime number.".format(number))
        isTrue = False
    return isTrue


# -------------2. ODEV - Sayinin Tam Bolenlerini Bulma-------------
def findDivisors(number):
    divisors = []
    for i in range(2, number//2+1):
        if number % i == 0:
            divisors.append(i)
    divisors.append(number)
    print('\nAll divisors of {} are: {}'.format(number, ', '.join(map(str, divisors))), end='')
    return divisors

# -------------3. ODEV - Mukemmel Sayi Bulma-------------
def isPerfect():
    print(
        "\nPerfect number, a positive integer that is equal to the sum of its "
        "proper divisors (all it's divisors excluding itself). "
        "\nFollowing are perfect numbers from 1-1000:\n")
    for number in range(1,1000):
        divisors = []
        for i in range(1, number // 2 + 1):
            if number % i == 0:
                divisors.append(i)
        divisors.append(number)

        sumOfDivisors = 0
        for i in divisors:
            sumOfDivisors += i
        if sumOfDivisors == 2*number:
            print("\n","\u2605" * 3 + " {} is a perfect number! ".format(number) + "\u2605" * 3, sep='')
        # else:
        #     print("\n", "{} is not a perfect number!".format(number), sep='')

# -------------4. ODEV - Iki Sayinin OBEB'ini Bulma-------------
# This function is written to be used for finding EBOB and EKOK
def isPrime(number):
    isTrue = True

    if number > 1:
        while isTrue:
            # See if the number is divisible by any other number than 1 and itself
            for i in range(2, number // 2 + 1):
                if number % i == 0:
                    isTrue = False
                    break
                elif i == 15:
                    isTrue = False
            else:
                isTrue = True
                break
    else:
        isTrue = False
    return isTrue

def EBOB(number1, number2):
    list1 = findDivisors(number1)
    list2 = findDivisors(number2)
    intList = list(set(list1) & set(list2))
    intList = [i for i in intList if isPrime(i)]
    ebob = 1
    print("\nCommon prime divisors of {} and {} are : ".format(number1, number2), ', '.join(map(str, intList)))
    for i in intList:
            ebob *= i

    # print('\nThe greatest common divisor of {} and {} is {}'.format(number1, number2, ebob))
    # print('intersection: ', intList)
    print("So the EBOB of {} and {} is: ".format(number1, number2), ebob)
    return ebob

# -------------5. ODEV - Iki Sayinin EKOK'unu Bulma-------------
def EKOK(number1, number2):
    if number1 > number2:
        ekok = number1
    else:
        ekok = number2

    while (True):
        if ((ekok % number1 == 0) and (ekok % number2 == 0)):
            break
        ekok += 1
    print("\nEKOK of {} and {} is : {} ".format(number1, number2, ekok))
    return ekok

# -------------6. ODEV - Sayinin Okunusunu Bulma-------------

def readNumbers(number):
    try:
        onesPron = ['', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz']
        tensPron = ['On', 'Yirmi', 'Otuz', 'Kirk', 'Elli', 'Altmis', 'Yetmis', 'Seksen', 'Doksan']
        if number // 10 == 0:
            raise IndexError
        else:
            tenPron = tensPron[number // 10 - 1]
        onePron = onesPron[number % 10]
        print('\n{} ---------->'.format(number), tenPron, onePron)
    except IndexError:
        print('\nYou must enter a two digit number!')

# -------------7. ODEV - Sayinin Okunusunu Bulma-------------
import math
def specialTriangle():
    triangleList=[]
    for a in range(1,101):
        for b in range(1,101):
            for c in range(1,101):
              if c**2==(a**2+b**2):
                sublist=[a,b,c]
                triangleList.append(sublist)
    # Following for loop is just to print every 10 items in the list in a new line
    # Otherwise the print doesn't fit in the screen
    print('\n')
    for i in range(len(triangleList) // 10 + 1):
        print(*triangleList[i * 10:(i + 1) * 10], "\n", sep='; ')
    return triangleList

# -------------8. ODEV - Sayinin Faktoriyelini Bulma-------------
def factorial(number):
    factor = 1
    for i in range(1, number+1):
        factor *=i
    print('\n{}! = {}'.format(number, factor))
    return factor

# -------------9. ODEV - Buyuk - Kucuk Harf Sayisini Bulma-------------
def CountUpperLower():
    text = input("\nPlease type a string to be processed: ")
    upperLetters = 0
    lowerLetters = 0

    for i in text:
        if i.isupper() == True:
            upperLetters += 1
        elif i.islower() == True:
            lowerLetters += 1
    print("Count of capital letters: ", upperLetters)
    print("Count of small letters: ", lowerLetters)



# -------------10. ODEV - Kelimeleri Alfabetik Siralama-------------
def orderWords():
    text = input("\nPlease type words seperated only by hyphen (-) ekleyerek birden fazla kelime yaziniz:\n")
    wordList = []
    wordList = text.split("-")
    wordList.sort()
    return print(*wordList, sep="-")

# -------------11. ODEV - Bir Listedeki Ozgun Elemanlari Ayirarak Listeleme-------------

def listUnique():
    itemList = input("\nMake a list by leaving spaces (e.g. 1 2 3 3 4 5 5) between list elements: ")
    itemList = list(itemList.split(" "))
    uniqueList = []
    for i in itemList:
        if i not in uniqueList:
            uniqueList.append(i)
    print("Your original list\t: {}\nList of Unique Items: {}".format(itemList,uniqueList))
    return uniqueList

# -------------12. ODEV - Tersten Aynimi-Degilmi Bulma-------------
# isReverseSame() and isReverseSame2() returns only True or False as they are now
# However, you can uncomment the print statements within if else blocks to get a more
# user friendly, easy to understand feedback.

def isReverseSame():
    # This function is case insensitive. So a = A
    userInput = input("\nEnter a text to check if it's the same from reverse: ")
    textLength = len(userInput)
    reverse = ''
    for i in range(textLength):
        reverse += userInput[textLength - 1 - i]
    # Sample entry: ey edip adanada pide ye
    if userInput.lower() != reverse.lower():
        # print('"{}" is read from reverse as:\n"{}" so is NOT the same!'.format(userInput.lower(), reverse.lower()))
        return False
    else:
        # print('"{}" is read from reverse as:\n"{}" so is the same!'.format(userInput.lower(), reverse.lower()))
        return True
# Below is the same function as above but written slightly differently
def isReverseSame2():
    userInput = input("\nEnter a text to check if it's the same from reverse: ")
    reverse = userInput[::-1]
    if userInput.lower() != reverse.lower():
        # print('"{}" is read from reverse as:\n"{}" so is NOT the same!'.format(userInput.lower(), reverse.lower()))
        return False
    else:
        # print('"{}" is read from reverse as:\n"{}" so is the same!'.format(userInput.lower(), reverse.lower()))
        return True


#  _____________________________________________________________________________
# |  To run any of the functions, just remove the preceding comment character # |
# |  and replace x, y where applicable with the desired input or uncomment      |
# |  the lines where input is asked (lines 212-214) to ask the user for a single|
# |  input or two inputs.                                                       |
# |_____________________________________________________________________________|

# x = int(input("\nEnter a two digit number: "))
# x = int(input("\nEnter the first number: "))
# y = int(input("\nEnter the second number: "))
# isPrimeNumber(x)  # Question 1
# findDivisors(x)   # Question 2
# isPerfect()       # Question 3
# EBOB(x,y)         # Question 4
# EKOK(x,y)         # Question 5
# readNumbers(x)    # Question 6
# specialTriangle() # Question 7
# factorial(x)      # Question 8
# CountUpperLower() # Question 9
# orderWords()      # Question 10
# listUnique()      # Question 11
# isReverseSame()   # Question 11 ----> Uncomment this line and print statements inside the function
# isReverseSame2()  # Question 11 ----> Uncomment this line and print statements inside the function
# print(isReverseSame())   # Question 11 ----> Uncomment this line just to get a True or False
# print(isReverseSame2())  # Question 11 ----> Uncomment this line just to get a True or False
