#Verilen bir listenin içindeki özgün elemanları ayırıp
# yeni bir liste olarak veren bir fonksiyon yazınız.
# Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]
def ozgun(*sayilar):

    liste=[sayilar]
    screen=[]
    print(liste)

    screen=[r for r in set(sayilar)]#kumeler ayni karakterleri berindirmadigi icin kumeye cevirip tekrar
                                    #listeye donusturuyoruz

    print(screen)
#-----------------------------------------------------



ozgun(1,2,33,4,1,1,1,1,33,44,8,8,8,8,99,8,8,8,85,6,6,66,7,4,5,5,5,4,7)
