##11. Verilen bir listenin içindeki özgün elemanları ayırıp
##yeni bir liste olarak veren bir fonksiyon yazınız.
##Örnek Liste : [1,2,3,3,3,3,4,5,5]
##Özgün Liste : [1, 2, 3, 4, 5]
def OzgunListe():
    OrnekListe = [1,2,3,3,3,3,4,5,5]
    OzgunListe = []
    for i in OrnekListe:
        if i in OrnekListe and i not in OzgunListe:
            OzgunListe += [i]     
    print(OzgunListe)
OzgunListe()

