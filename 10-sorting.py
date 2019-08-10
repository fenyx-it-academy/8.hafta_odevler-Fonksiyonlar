def sorting(items):
    items = items.split("-")
    items = sorted(items)
    items = "-".join(items)
    return items
print("*"*15, "SORTING ITEMS", "*"*15)

try:
    while True:
        letter_list = []
        items = input("Please enter the words with write '-' between them:")
        for let in items:
            letter_list += [let]
        if "-" not in letter_list:
            print("\n-->Please enter words more than one and split them with '-'\n")
        else:
            print(sorting(items))
            break
except:
    print("Error, please try again")
