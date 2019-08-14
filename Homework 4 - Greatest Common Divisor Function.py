print("********** Greatest Common Divisor **********\n\n")
def gcd(x=1,y=1):
    aliquats_x=set()
    aliquats_y=set()
    for i in range(1,x+1):
        if x%i==0:
            aliquats_x.add(i)
    for i in range (1,y+1):
        if y%i==0:
            aliquats_y.add(i)
    gcd1=aliquats_x.intersection(aliquats_y)
    return max(gcd1)
while True:
    x=input("Please enter first number you would like to calculate GCD.\n")
    y=input("Please enter second number you would like to calculate GCD.\n")
    if x.isdigit() and y.isdigit():
        x=int(x)
        y=int(y)
        print(gcd(x,y))
        while True:
            q=input("""Would you like to quit? If yes please press "q", For new calculation, please press "ENTER".
""")
            if q.lower()=="q":
                print("Program terminated.")
                exit()
            elif not q:
                break
            else:
                print("You made an incorrect entry. Please check and read instructions!!!")
    else:
        print("You made an incorrect entry. Please check and read instructions!!!")
