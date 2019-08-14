print("********** Aliquat Function **********")
def aliquat(args):
    aliquats=[]
    for i in range(1,args+1):
        if args%i==0:
            aliquats.append(i)
    return aliquats
while True:
    while True:
     x=input("Please enter a number you would like to find the aliquots.\n")
     if x.isdigit():
        x=int(x)
        print(*aliquat(x))
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
 
