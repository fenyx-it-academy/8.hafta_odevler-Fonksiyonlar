print("********** Perfect Number Function **********")
def perf_number(x):
    aliquats=0
    perfect=[]
    for k in range(1,x+1):
        for i in range (1,k):
            if k%i==0:
                aliquats+=i
        if aliquats ==k:
            perfect.append(k)
            aliquats=0
        else:
            aliquats=0
    print("These are the perfect numbers between 1 and 1000:",perfect,"\n")
def perf_number1(args):
    aliquats=[]
    for i in range(1,args):
        if args%i==0:
            aliquats.append(i)
    if sum(aliquats)==args:
        return print(args,"is a perfect number")
    else:
        return print(args, "is not a perfect number")
perf_number(1000)
q=input("""To query numbers greater than thousand, please press "ENTER",
To quit the program,please press "q".
""")
if q.lower()=="q":
    print("Program terminated.")
    exit()
elif not q:
    pass
else:
    print("You made an incorrect entry. Please check and read instructions!!!")
while True:
    while True:
     x=(input("Please enter a number greater than a thousand you would like to know if it is a perfect number.\n"))
     if x.isdigit()and int(x)>1000:
        x=int(x)
        perf_number1(x)
        break
     else:
        print("You made an incorrect entry. Please enter a number greater than a thousand!!!")
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



 
