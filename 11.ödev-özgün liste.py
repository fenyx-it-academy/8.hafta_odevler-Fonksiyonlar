def ozgunliste(a):

    liste = []
    for i in a:
        if i not in liste:
            liste.append(i)

    return liste

onerilen_liste = [1,2,5,7,6,6,9,45,54,25,12,35,1,7,25,'a','a','b',[3,4],[4,3]]

print(ozgunliste(onerilen_liste)) 
