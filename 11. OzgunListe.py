# Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
# Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]

try:
    newListe = []

    def ozgunListe(list):
        for i in list:
            if i not in newListe:
                newListe.append(i)
        newListe.sort()
        print(newListe)


    ozgunListe([1, 1, 2, 2, 5, 4, 8, 7, 5, 1, 7, 4, 6, 9, 8, 9, 3, 5])
except:
    print('Hatali islem. Program sonlandirildi.. ')