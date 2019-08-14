print("********** Upper and Lower Case **********\n\n\n")
def up_low(args):
    up=0
    low=0
    for i in args:
        if i.islower():
            low+=1
        elif i.isupper():
            up+=1
        else:
            pass
    return print(f"There are {up} upper case and {low} lower case letters.")
while True:
    data=input("Please enter the word or phrase you would like to find how many lower and uppercase letters it contains.\n")
    up_low(data)
    while True:
     q=input("""Would you like to quit? If yes please press "q", if no please press "ENTER".
""")
     if q.lower()=="q":
        print("Program terminated.")
        quit()
     elif not q:
        break
     else:
        print("You made an incorrect entry. Please check and read instructions!!!")
 
            
