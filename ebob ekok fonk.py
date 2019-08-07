#Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB)
# dönen bir tane fonksiyon yazın.
def ebob(sayi_1=int(input('1.sayiyi giriniz:')),sayi_2=int(input('2.sayiyi giriniz:'))):

    k1=[]                       #sayi_1 pozitif bolenleri icin liste 
    k2=[]                       #sayi_2 pozitif bolenleri icin liste
    for s1 in range(1,sayi_1+1):#sayi_1 in +1 fazlasi alindiki kendisinide bolsun 
        if sayi_1 % s1==0:
            k1+=[s1]            #sayi_1 in pozitif bolenleri 

    for s2 in range(1,sayi_2+1):#sayi_2 in +1 fazlasi alindiki kendisinide bolsun 
        if sayi_2 % s2==0:      #sayi_2 in pozitif bolenleri 
            k2+=[s2]


    ebob=max(set(k1)&set(k2))   #k1 ve k2 kumeye donusuturuldu ve kesisim kumesi bulunuldu
                                #bu kumedeki en yuksek sayi ebob dur
    ekok=(sayi_1*sayi_2)/ebob   #ekok=(a.b)/ebob dur
    
    print('{} ve {} sayisinin ebob  {} ekok {} dur.'.format(sayi_1,sayi_2,ebob,ekok))
ebob()#kumelerrin ortak eleman(kesisim)kumesinden yararlandik
