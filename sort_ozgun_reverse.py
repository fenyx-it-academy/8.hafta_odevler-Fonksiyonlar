########################################################################################
print("Kelime Duzenleme programi\nBu program girilen kelimeleri alfabetik siraya gore duzenler.")
def duzen():
    girdi=input("Lutfen Siralamak istediginiz kelimeleri aralarina tire(-) koyarak giriniz:")
    girdi1=girdi.lower()
    i=girdi1.split("-")
    i.sort()
    print(i)
duzen()

#####################################################################################
def ozgun():
    liste=[2,3,4,3,2,3,4,3,4,5,4,5,6,56,756,56,45,54]
    ozgun=[]
    for i in liste:
        if i not in ozgun:
            ozgun.append(i)
    return print(ozgun)
ozgun()



#########################################################################################
def reverse_ask():
    while True:
        word=input("enter a word to ask reversed is same:")
        reword=[]
        for i in word:
            reword.append(i)
        if reword[::-1]==reword:
            print("congrats;",word,"is same reversed.")
        else:
            print(word,"is not same when reversed.")
reverse_ask()
