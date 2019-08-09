# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:29:02 2019

@author: HP
"""

# 1)Asal sayi olup olmadigini kontrol eden fonksiyon yazınız.

while True :
    cik=input("Cikmak icin q ye basiniz, asal sayi belirlemek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
   
    sayi=int(input("Asal olup olmadigini belirlemek istediginiz pozitif tamsayi giriniz...; "))
            
    def asal(sayi):
        if sayi>=2 :
            if sayi == 2:
                print("2 sayisi asaldir..!")
            x=2
            count=0
            while x < sayi :
                sonuc = sayi % x
                x +=1
                if sonuc ==0 :
                    count=0
                    print(sayi,"sayisi asal degildir..!")
                    break     
                elif sonuc !=0 :
                    count=1
            if count==1 :
                print(sayi,"sayisi asaldir..!")
                
        else :
            print("2 den buyuk tamsayi giriniz.")
    asal(sayi)
    
            

      

# %%
# 2) Bir sayinin tam bolenlerini bulan fonksiyon yazınız...

while True :
    cik=input("Cikmak icin q ye basiniz, tam bolenleri belirlemek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    sayi=int(input('Bir sayi giriniz...;' ))
    
    def tam_bolen(sayi):
        liste=[]
        x=1
        for x in range(sayi):
            if sayi % (x+1) == 0:
                liste +=[x+1]
            else:
                pass
        for i in range(len(liste)):
            liste.append(-liste[i])
        return liste
            
    print(tam_bolen(sayi))
# %%
# 3) Mukemmel SAYI
#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
#Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın. 
#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. 
#Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

while True :
    cik=input("Cikmak icin q ye basiniz, mukemmel sayilar belirlemek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break

    number=int(input('Hesaplanacak mukemmel sayilariniz icin mukemmel bir sinir belirleyiniz ; '))
    
    for sayi in range(2,number+1):
        def mukemmel(sayi):
            liste=[]
            sumtop=0
            
            for x in range(sayi):
                if sayi % (x+1) == 0:
                    liste +=[x+1]
            
            for i in range(len(liste)):
                sumtop+=liste[i]
                
            if sumtop==2*sayi:
                print(f'{sayi}','mukemmel sayidir')
        
        mukemmel(sayi)

# %%
# 4) OBEB
#Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

while True :
    cik=input("Cikmak icin q ye basiniz,obeb belirlemek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    else:
        print('Iki pozitif tamsayi giriniz ...;')
    sayi1=int(input('Birinci sayi ; '))
    sayi2=int(input('Birinci sayi ; '))
    
    def ebob(sayi1,sayi2):
        if sayi1<sayi2:
            kucuk=sayi1
        else:
            kucuk=sayi2
        liste=[]
        for i in range(kucuk):
            if sayi1%(i+1)==0 and sayi2%(i+1)==0:
                liste+=[i+1]
                
        liste.sort()
        if len(liste)==1:
            return f"{sayi1} ve {sayi2} sayilari aralarinda asaldir."
        return f"{sayi1} ve {sayi2} nin ebob u {liste[-1]} dir."
    
    print(ebob(sayi1,sayi2))

        
            

# %%
# 5) OKEK
#Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

while True :
    cik=input("Cikmak icin q ye basiniz, okek belirlemek icin enter a basiniz ; ")
    if cik=='q':
        print('Cikiliyor...')
        break
    else:
        print('Iki pozitif tamsayi giriniz ...; ')

    sayi1=int(input('Birinci sayi ; '))
    sayi2=int(input('Ikinci sayi ; '))
    
    def ekok(sayi1,sayi2):
        if sayi1>sayi2:
            buyuk=sayi1
        else:
            buyuk=sayi2
        
        while True:
            if buyuk%sayi1==0 and buyuk%sayi2==0:
                ekok=buyuk
                break
            else:
                buyuk+=1
                
        return f"\n{sayi1} ve {sayi2} nin ekok u {ekok}' dir"
    
    print(ekok(sayi1,sayi2))



