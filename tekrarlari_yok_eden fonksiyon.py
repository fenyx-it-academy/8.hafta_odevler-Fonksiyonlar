"""
11. Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
Örnek Liste :  Özgün Liste : [1, 2, 3, 4, 5]
"""
def ozgun_eleman():
    liste=[1,2,3,3,3,3,4,5,5]
    yeni_liste=[]
    for i in liste:
        if i not in yeni_liste:
            yeni_liste.append(i)
    return yeni_liste
print(*ozgun_eleman())