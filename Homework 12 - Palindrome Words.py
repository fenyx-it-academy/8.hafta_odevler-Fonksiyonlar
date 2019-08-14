print("********** Palindrome Words *********")
def palindrome(args):
    entry=""
    output=""
    for i in args:
        if i.isalpha():
            entry+=i
        else:
            pass
    for i in reversed(entry):
        output+=i
    if entry == output:
        return print(True)
    else:
        return print(False)
while True:
 args=input("Please enter a word you would like to know if it is a palindrome word.\n")
 palindrome(args)
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
    
