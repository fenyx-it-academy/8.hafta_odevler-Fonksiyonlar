print("********** Least Common Multiple **********\n\n")
def lcm(x=1,y=1):
    aliquats=1
    if x>=y:
     if x%y==0:
         return x
     else:
      for i in range(1,x):
        if x%i==0 and y%i==0:
                aliquats*=i
    else:
     if y%x==0:
         return y
     else:  
      for i in range(1,y):
        if x%i==0 and y%i==0:
            aliquats*=i
    lcm1=aliquats*(x//aliquats)*(y//aliquats)
    return lcm1 
while True:
    x=input("Please enter first number you would like to calculate LCM.\n")
    y=input("Please enter second number you would like to calculate LCM.\n")
    if x.isdigit() and y.isdigit():
        x=int(x)
        y=int(y)
        print(lcm(x,y))
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
