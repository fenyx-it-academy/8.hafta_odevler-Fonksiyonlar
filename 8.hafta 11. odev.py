print('b.')
'''
11-Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]
ornek_liste = [1,2,3,3,3,3,4,5,5]
'''
def ozgun():
    veri=input("ozgun liste olusturmak istediginiz verinizi giriniz : ")
    ozgun_list=[]       # bos listemizi olusturduk
    for i in veri:      # verimizdeki degerlere for ile baktik
        if i not in ozgun_list:  # tekrar edenlerri ayirdik...listemizde olmayanlari ekledik
            ozgun_list.append(i)
    return ozgun_list
print(ozgun())