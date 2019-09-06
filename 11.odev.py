def ozgun(*deger):
    liste = []
    for i in deger:
        liste.append(i)
    kume=set(liste)
    liste=list(kume)
    return liste

print(ozgun(1,1,2,33,44,33,44,55,66,55,6,33,4,567,887,65,65))
