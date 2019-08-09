""""Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
Örnek Liste : [1,2,3,3,3,3,4,5,5]
Özgün Liste : [1, 2, 3, 4, 5]"""
def ozgunfonksiyon():
    liste1 = [1,6,8,4,6,6,9,0,8,3,4,5]
    liste2 = set(liste1)#ayni degerleri yazmamasi icin ikinci listemizi kume olarak tanimliyoruz
    for i in liste1:#liste1 deki her bir degeri yeni listemize gonderiyoruz
        liste2.add(i)
    print(liste2)
ozgunfonksiyon()