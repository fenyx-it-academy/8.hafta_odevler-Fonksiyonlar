print("********** Convertor **********")
a={"0":" ", "1": "one", "2" : "two", "3" : "three", "4" : "four", "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine"}
b={10 : "Ten",11 : "Eleven",12 : "Twelve",13 : "Thirteen",14 : "Fourteen",15 : "Fifteen",16 : "Sixteen",17 : "Seventeen",18 : "Eighteen",19 : "Nineteen"}
c={"2" : "Twenty","3" : "Thirty","4" : "Forty","5" : "Fifty","6" : "Sixty","7" : "Seventy","8" : "Eighty","9" : "Ninety"}
def conv(args):
    if args[0]=="1":
        return b[int(args)]
    else:
        return c[args[0]]+" "+a[args[1]]
while True:
    x=input("Please enter two digit number you would like to convert.\n")
    if x.isdigit() and len(x)==2:
        print(conv(x))
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

