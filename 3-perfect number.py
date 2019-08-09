def perfect():
    number_list = []
    for number in range(1,1000):
        divisors = []
        for num in range(1,number):
            if number % num == 0:
                divisors += [num]
        sum_list = sum(divisors)
        if sum_list == number:
            number_list += [number]
    return number_list

print(perfect())
