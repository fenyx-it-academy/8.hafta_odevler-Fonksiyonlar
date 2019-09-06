def ters(*deger):
    liste = []
    for i in deger:
        print(type(i))
        if i==i[::-1]:
            liste.append("True")
            continue
        else:
            liste.append("False")
            continue
    return print(liste)

ters("selma","elma","kasik","saat","madam","lal")
