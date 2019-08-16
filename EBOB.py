
  #bu kod bir sayinin tam bolenlerini bulur
def tambolenler(sayi):
    bolenler = []  # tam bolenleri icine atmak icin bos bir liste olusturur
    for i in range(1, sayi+1):  # 1 ve sayi dahil bu araliktaki sayilara bakar
        if sayi % i == 0:  # bu araliktaki tam bolen sayilari bulur
            bolenler.append(i)  # tam bolen sayilari bolenler listesinde biriktirir
    return bolenler



            #EBOB ve EKOK una bakilacak iki sayi gerekli
sayi1=int(input("birinci sayi:"))
sayi2=int(input("ikinci sayi:"))

sayi1tambolen=tambolenler(sayi1)        #birnci sayiyi kalansiz bolen sayilarin listesi
sayi2tambolen=tambolenler(sayi2)        #ikinci sayiyi kalansiz bolen sayilarin listesi
ortakbolen=[]                           #iki listede ortak olan elemanlari bu listenin icne atalim

#ortak bolenleri bulma islemi
for i in sayi1tambolen:
    if i in sayi2tambolen:          #birinci listenin elemanlarindan ikinci listede olanlari bulalim.
        ortakbolen.append(i)        #bulunan her elemani ortak bolen listesinde biriktirelim.
ortakbolen.sort()                   #bu listeyi kucukten buyuge siralayalim

if ortakbolen!=[1]:
    print(ortakbolen[-1],'sayisi bu iki sayinin EBOB dir')          #bu listenin en sondaki elemani(en buyugu)EBOB dur
    print(ortakbolen[1],'sayisibu iki sayinin EKOK dir')            #bu listede 0.index de 1 var.o yuzden 1.index e baktik
else:
    print("bu iki sayinin ebob ve ekok u 1 dir.aralarinda asaldir")
