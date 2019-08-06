##Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak
##veren bir fonksiyon yazınız. Örnek Liste : [1,2,3,3,3,3,4,5,5]
##Özgün Liste : [1, 2, 3, 4, 5]

def ozgunliste(a):
    liste=[]
    for i in a:
        if i not in liste:
            liste.append(i)
    return liste

verilen_liste=[1,2,5,7,6,6,9,45,54,25,12,35,1,7,25,'a','a','b',[3,4],[4,3]]
print(ozgunliste(verilen_liste))
