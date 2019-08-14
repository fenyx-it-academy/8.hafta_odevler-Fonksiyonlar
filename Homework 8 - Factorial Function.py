print("********** Factorial Function **********\n\n\n")
def fact(args):
    x=1
    for n in range(1,args+1):
        x=x*n
    return print(x)
    
while True:
    while True:
     x=(input("Please enter a positive number you would like to calculate factorial.\n"))
     if x.isdigit():
        x=int(x)
        fact(x)
        break
     else:
        print("You made an incorrect entry. Please enter only positive number!!!")
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
 
        
    
