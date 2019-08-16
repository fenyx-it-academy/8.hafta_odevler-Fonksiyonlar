#bu kod bir sayinin tam bolenlerini bulur


sayi=int(input("tam bolenlerini bulmak icin lutfen bir sayi giriniz:"))    #sayi kullanicidan ister.

bolenler=[]                                  #tam bolenleri icine atmak icin bos bir liste olusturur
for i in range(1,sayi+1):                    #1 ve sayi dahil bu araliktaki sayilara bakar
    if sayi%i==0:                            #bu araliktaki tam bolen sayilari bulur
        bolenler.append(i)                   #tam bolen sayilari bolenler listesinde biriktirir
print(bolenler)                               #tam bolen sayilar listesini yazdirir
