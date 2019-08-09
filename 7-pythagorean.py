def pythagorean():
    pow_list = []
    
    for num in range(1, 100):
        for num2 in range(1, 100):
            sum_pow = pow((pow(num, 2) + pow(num2, 2)), 0.5)
            if sum_pow.is_integer() and sum_pow <= 100:
                pow_list += [[[num, num2], sum_pow]]
    for i in pow_list:
        print(*i)
    return pow_list
                
pythagorean()
