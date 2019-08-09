# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:35:31 2019

@author: HP
"""

# %%
# 9) Buyuk Kucuk Harf
#Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf sayılarının veren bir fonksiyon yazınız.

while True :
    cik=input("Cikmak icin q ye basiniz, devam etmek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    else:
        print('Buyuk ve Kucuk harf bulan program ...; ')

    soz=input("Cumle ya da kelime giriniz ;")

    def harf(soz):
        a=0;b=0;c=0;d=0
        for i in soz :
            if i.islower() ==True :
                a+=1
            elif i.isupper() == True :
                b+=1
            elif i.isdigit()==True :
                c+=1
            elif i.count(" ") :
                pass
            else : 
                d+=1
        return f'{a} tane kucuk harf, {b} tane buyuk harf, {c} tane rakam ve {d} tane ozel karakter vardir'
    print(harf(soz))


# %%
# 10) Tire li Taralelli...
#Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve sonrasında bu kelimeleri harf sırasına göre dizip
#tekrar tire ile ayırıp output olarak veren bir fonksiyon yazınız. 
#örnek girdi: green-red-yellow-black-white örnek çıktı: black-green-red-white-yellow

while True :
    cik=input("Cikmak icin q ye basiniz, devam etmek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    else:
        print('Tire(-) ile ayrılan bir input dizisi giriniz ...; ')

    soz=input("Bir soz dizisini aralarda '-' olacak sekilde giriniz ==> ")
    
    def diz(soz):
        liste=soz.split('-')
        kume=sorted(liste)
        return kume
        
    print(*diz(soz), sep='-') 

