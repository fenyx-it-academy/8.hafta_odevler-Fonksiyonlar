def gre_com_div(number1, number2):
    div_list_1 = []
    div_list_2 = []
    list_3 = []

    for num in range(1,number1+1):
        if number1 % num == 0:
            div_list_1 += [num]
    for num in range(1,number2+1):
        if number2 % num == 0:
            div_list_2 += [num]
    for item in div_list_1:
        if item in div_list_2:
            list_3 += [item]
    return max(list_3)
try:
    print("*"*15,"CHECK THE GREATEST COMMON DIVISOR","*"*15) 
    number1 = int(input("Please enter first number:"))
    number2 = int(input("Please enter other number:"))
    if number1 < 1 or number2 < 1:
        print("You cannot choose this numbers")
    print(f"The greatest common divisor is {gre_com_div(number1, number2)}")
except ValueError:
    print("Try again and please enter positive number")
except:
    print("Error,please try again")
