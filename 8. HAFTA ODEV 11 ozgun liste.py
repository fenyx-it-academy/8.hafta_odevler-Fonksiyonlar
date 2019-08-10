def ozgun():
    liste=["M","M",23,23,633,45,45,5,6,6]
    print("eski liste: ",liste)
    yeni=[]
    for i in liste:
        if i not in yeni:
            yeni.append(i)
    return yeni
print("ozgun liste: ",ozgun())
