def least_com_mul(number1, number2):
    multiple_1 = []
    multiple_2 = []
    common = []
    if number1 < 1 or number2 < 1:
        return "Please do not enter number below 1"
    for num in range(1, number2 + 1):
        mul = number1 * num
        multiple_1 += [mul]
    for num in range(1, number1 + 1):
        mul = number2 * num
        multiple_2 += [mul]
    for item in multiple_1:
        if item in multiple_2:
            common += [item]
    return min(common)
try:
    print("*"*15,"Least Common Multiple","*"*15)
    number1 = int(input("Please enter first number:")) 
    number2 = int(input("Please enter other number:"))
    print(f"The least common multiple is {least_com_mul(number1, number2)}")
except ValueError:
    print("please enter a number")
except:
    print("Error,please try again")
