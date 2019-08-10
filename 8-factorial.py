def factorial(number):
    digit = 1
    if number < 0:
        return "Please don't enter below 0"
    for num in range(2,number+1):
        digit = digit * num
    return digit
print(factorial(5))
