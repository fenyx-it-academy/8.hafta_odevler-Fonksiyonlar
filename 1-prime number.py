def prime(number):
    if number < 2:
        return "You cannot check this number"
    for num in range(2,number):
        if number % num == 0:
            return f"{number} is not prime number"
    return f"{number} is prime number"
                
print(prime())
