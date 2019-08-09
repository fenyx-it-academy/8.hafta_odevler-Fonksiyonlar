#odev 11#
#tek elemanlı liste olusturuyoruz #

def ozgun():
    liste=[1,2,3,3,3,3,4,5,5]
    print("eski liste: ",liste)
    yeni=[]
    for i in liste:
        if i not in yeni:
            yeni.append(i)
    return yeni
print("ozgun liste: ",ozgun())
