# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:38:20 2019

@author: HP
"""

# %%
# 11) OZGUN Liste
#Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız. 
#Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]

while True :
    cik=input("Cikmak icin q ye basiniz, ozgun eleman belirlemek icin enter'a basiniz... ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    
    veri=input('Liste olacak veri giriniz...;')
    def ozgun(veri):
        liste=list(veri)
        cumle=set(liste)
        yeni_liste=list(cumle)
        yeni_liste.remove(' ')
        return sorted(yeni_liste)
    print('Ozgun elemanlar listesi ;',ozgun(veri))



# %%
# 12) TERS OKUMA
#Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız. 
#örnek: madam, taco cat, utrecht sonuç: True, True, False

while True :
    cik=input("Cikmak icin q ye basiniz, Tersten okuma kontrolu icin enter'a basiniz... ; ")
    if cik=='q':
        print('Cikiliyor...')
        break

    veri=input('Kontrol edilmesini istediginiz veriyi giriniz...;')
    
    def kontrol(veri):
        count=0
        global liste
        liste=list(veri)
        for i in range(len(liste)):
            if liste[i]==liste[-(i+1)]:
                count=1
            else:
                count=2
        if count==1:
            print('True')
        elif count==2:
            print('False')
        #else:
            #continue
    kontrol(veri)  
    