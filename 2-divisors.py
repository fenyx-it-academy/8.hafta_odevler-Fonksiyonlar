def divisor(number):
    divisors = []
    for num in range(1,number+1):
        if number % num == 0:
            divisors += [num]
    return divisors
print(divisor(12))
