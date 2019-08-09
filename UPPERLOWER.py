print("*******UPPER and lower detecting programme********")
def upper_smaller():
    big=0
    small=0
    text=input("Please Write something:")
    for i in text:
        if i.islower():
            small+=1
        elif i == " ":
            pass
        elif i.isdigit() is True:
            pass
        else:
            big+=1
    print("big letters=",big,"small letters=",small)
upper_smaller()