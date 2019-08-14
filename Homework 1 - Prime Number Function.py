print("********** Prime Number **********\n\n\n")
def prime_number(args):
    if args<=1:
        return print(args,"is not a prime number.")
    else:
        count=False
        for i in range(2,args):
            if args%i==0:
                count=True
                break
            else:
                pass
        if count==False:
            return print(args,"is a prime number")
        else:
            return print(args,"is not a prime number")
while True:
    while True:
     try:
         x=int(input("Please enter a number you would like to know if it is a prime number.\n"))
         prime_number(x)
         break
     except ValueError:
         print("You made an incorrect entry. Please enter only number!!!")
         continue
    while True:
     q=input("""Would you like to quit? If yes please press "q", if no please press "ENTER".
""")
     if q.lower()=="q":
        print("Program terminated.")
        exit()
     elif not q:
        break
     else:
        print("You made an incorrect entry. Please check and read instructions!!!")
 
        
    
