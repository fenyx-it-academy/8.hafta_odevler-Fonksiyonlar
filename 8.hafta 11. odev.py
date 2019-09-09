print('b.')
'''
11-Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]
ornek_liste = [1,2,3,3,3,3,4,5,5]
'''
def ozgun(*args):
    veri=input("ozgun liste olusturmak istediginiz verinizi giriniz : ")
    ozgun_list=[]                   # bos listemizi olusturduk
    for i in veri.split(','):
        ozgun_list.append(i)
    ozgun_list=set(ozgun_list)      # listemizi kumeye cevirdik icindeki tekrar edenleri ayirdik
    return list(ozgun_list)
print(ozgun())
