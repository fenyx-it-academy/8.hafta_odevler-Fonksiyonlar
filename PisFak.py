# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:33:22 2019

@author: HP
"""

# %%
# 6) Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın. 
#Örnek: 97 ---------> Doksan Yedi

while True :
    cik=input("Cikmak icin q ye basiniz, devam etmek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    else:
        print('iki basamakli sayinin okunusuna yazan program...')
    
    try :

        ab=input("Iki basamakli pozitif bir sayi girini ; ")
        
        Birler={'0':'Sifir','1':'Bir','2':'Iki','3':'Uc','4':'Dort','5':'Bes','6':'Alti','7':'Yedi','8':'Sekiz','9':'Dokuz'}
        Onlar={'10':'On','20':'Yirmi','30':'Otuz','40':'Kirk','50':'Elli','60':'Altmis','70':'Yetmis','80':'Seksen','90':'Doksan'}
        neg=''
        if int(ab)<0:
            ab=str((-1)*int(ab))
            neg='eksi'
        if len(ab)>2:
            print('Iki basamakli sayilar giriniz...')
            continue
        def yazi(ab):
            a='';b=''
            kume=list(ab)
            onlar=str(int(kume[0])*10)
            if onlar in Onlar:
                n=Onlar[onlar]
                if neg=='eksi':
                    a='Eksi '+n
                else:
                    a=n
            birler=kume[1]
            if birler in Birler:
                b=Birler[birler]
                
            return f'{ab} ===> {a} {b}'
        
        print(yazi(ab))
    except :
        print('Yalnizca iki basamakli sayilar giriniz...')
# %%
# 7) PISAGOR
#1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.
#(a <= 100,b <= 100)
print("1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon")
print('Hipotenus 100 den buyuk olabilir ! ama dikkenarlar 101 den kucuk!')        
def pisagor():
    d=0
    for a in range(3,101):
        for b in range(4,101):
            if a<b:
                d=a**2+b**2
                c=d**(1/2)
                if c in range(5,150):
                    c=int(c)
                    print(f'{a},{b},{c} sayilari Pisagor u saglar')
                else:
                    continue
pisagor()

# %%
# 8) Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.

while True:
    cik=input("Cikmak icin q ye basiniz, devam etmek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    else:
        print('Faktoriyel hesabi yapan programa hosgeldiniz!...')

    try :    
        sayi=int(input("Faktoriyel hesabini istediginiz Pozitif bir sayi giriniz ...: "))
        if sayi<0:
            print('0 ve daha buyuk sayilarin faktoriyeli hesaplanir!')
            continue
        
        def faktor(sayi):
            fak=1
            for i in range(sayi):
                fak*=(i+1)
            return f'{sayi}!={fak}'
        
        print(faktor(sayi))
    except:
        print('Pozitif sayi giriniz...!')
        
