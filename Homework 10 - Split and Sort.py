print("********** Split and Sort Function **********")
def split_sort(args):
    data=entry.split("-")
    data.sort()
    output=[]
    for i in data:
        output.append(i)
    output="-".join(output)
    return (print(output))    
while True:
 entry=input("Please enter words separated by dashes.\n")
 if not entry:
     print("You made an incorrect entry. Please check and read instructions!!!")
 else:
     split_sort(entry)
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
 

