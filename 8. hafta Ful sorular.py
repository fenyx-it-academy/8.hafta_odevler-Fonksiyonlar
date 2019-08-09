###1.soru

print("""
                    Asal Sayi
                Kontrol Programina
                   Hosgeldiniz!!!
                   
            Asal sayi olup olmadigini
        merak ettiginiz bir sayiyi asagida
        yazip kontrolunu yapabilirsiniz.

    
        """)
def Asalsayikontrol(sayi):
    if(sayi>1):
        for i in range(2,sayi):
            if(sayi%i==0):
                return False
        return True
    else:
        return False
        
while (True):
    Asal=Asalsayikontrol(int(input("Kontrol etmek istediginiz sayiyi giriniz: ")))

    if Asal<1:
        print("1'den kucuk sayilarin kontrolu yapilamiyor.")
    if Asal==True:
        print("\nAsal sayidir...\n")
        continue
    else:
       print("\nAsal degildir...\n")
       continue


###2.soru
print("""
            Tam Bolenlerini Bulma Programi
        
        Herhangi bir sayinin tam bolenlerini
        elde etmek istiyorsaniz bu programi
            kullanarak gorebilirsiniz.

            Cikmak icin "q"ya basiniz...
        """)
def tambolenleribul(sayi):
    tambolenler=[]
    for i in range(2,sayi):
        if (sayi%i==0):
            tambolenler.append(i)
    return tambolenler
while True:
    sayi=input("\nTam bolenlerini gormek istediginiz sayiyi giriniz: ")
    if sayi=="q" or sayi=="Q":
        print("\nProgramdan cikiliyor.")
        quit()
    else:
        sayi=int(sayi)
        print("\nBu sayinin tam bolenleri: ",tambolenleribul(sayi))
        continue


###3.soru
print("""
        Mukemmel Sayi Programi
        
        Bir sayinin tam bolenlerinin toplami
    kendisine esitse o sayiya "Mukemmel Sayi"
    diyebiliriz. 1-1000 arasindaki Mukemmel
        Sayilari asagida gorebilirsiniz...

    """)


def mukemmelsayi(sayi):
    toplam=0
    for i in range(1,sayi):
        if (sayi%i==0):
            toplam+=i
    return toplam==sayi
for i in range(1,1001):
    if (mukemmelsayi(i)):
        print("1 ile 1000 arasindaki Mukemmel sayilar:",i)



###4.soru
print("""
            İki sayinin Ebob'unu Bulma
       Herhangi iki sayinin ortak bolenlerinin
       en buyugunu bulmak icin asagidaki programi
               kullanabilirsiniz....
               """)

def Ebob_bul(sayi1,sayi2):   
    i=1
    ebob=1
    while (i<=sayi1) and (i<=sayi2):

        if (not(sayi1%i) and not(sayi2%i)):
            ebob=i
        i+=1
    return ebob
while True:   
    sayi1 = int(input("1.sayiyi giriniz: "))
    sayi2 = int(input("2.sayiyi giriniz: "))
    if sayi1<1 or sayi2<1:
        print("\nLutfen 1'den buyuk sayilarin Ebob'unu bulmaya calisiniz.\n")
        continue
    else:
        print("\n",sayi1,"ve",sayi2,"sayilarinin Ebob'u: ",Ebob_bul(sayi1,sayi2),"\n")
        continue



###5.soru
print("""
            İki sayinin Ekok'unu Bulma
       Herhangi iki sayinin ortak katlarinin
       en kucugunu bulmak icin asagidaki programi
               kullanabilirsiniz....
               """)
def Ekok_bul(sayi1,sayi2):    
    i=2
    ekok=1
    while True:
        if (sayi1%i==0) and (sayi2%i==0):
            ekok*=i

            sayi1//=i
            sayi2//=i

        elif (sayi1%i==0) and (sayi2%i!=0):
            ekok*=i
            sayi1//=i

        elif (sayi1%i!=0) and (sayi2%i==0):
            ekok*=i
            sayi2//=i
            
        else:
            i += 1
        if (sayi1==1) and (sayi2==1):
            break
    return ekok
while True:
    sayi1 = int(input("1.sayiyi giriniz: "))
    sayi2 = int(input("2.sayiyi giriniz: "))
    if sayi1<1 or sayi2<1:
        print("\nLutfen 1'den buyuk sayilarin Ebob'unu bulmaya calisiniz.\n")
        continue
    else:
        print("\n",sayi1,"ve",sayi2,"sayilarinin Ekok'u: ",Ekok_bul(sayi1,sayi2),"\n")
        continue



###6.soru
print("""
            İki Basamakli Sayilarin Okunusu
            
        Herhangi iki basamakli bir sayinin okunusunu
            veren programa hosgeldiniz...

            Cikmak icin "q"ya basiniz...
            """)

birler=["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar=["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunusubul(sayi):
    birinci=sayi%10
    ikinci=sayi//10
    
    return onlar[ikinci] + " " + birler[birinci]

while True:
    sayi=input("İki basamakli bir sayi giriniz:")
    if sayi=="q" or sayi=="Q":
        print("Cikiliyor...\n")
        quit()
    else:
        sayi=int(sayi)
        if sayi>99 or sayi<10:
            print("Lutfen sadece iki basamakli sayi giriniz...\n")
            continue
        else:
            print(sayi,"sayisinin okunusu: ",okunusubul(sayi),"\n")



###7.soru
print("""
            Pisagor Ucgeni Olusturan Sayilar

        1 ile 100 arasindaki sayilardan Pisagor Ucgeni
            olusturanlari asagida listeledik...

        """)
def pisagor_bulma():
    
    pisagor_listesi=[]
    for a in range(1,101):
        for b in range(1,101):
            if a<=b:
                c=(a**2+b**2)**0.5
                if (c==int(c)):
                    pisagor_listesi.append((a,b,int(c)))
    return pisagor_listesi

for i in pisagor_bulma():
    print("Pisagor ucgeni: ",i)



###8.soru
#Faktoriyel Programi
print("""
                FAKTORIYEL PROGRAMI
         Herhangi bir sayinin faktoriyelini
        yani kendisinden 1'e kadar olan
        sayilarinin carpimini ogrenmek icin
         bu programi kullanabilirsiniz...

            Cikmak icin "q"ya basiniz...

        """)
#onecelikle fonsiyon olusturup yapmak istedigimiz islemi tanımlıyoruz.
def faktoriyel(sayi):
    if sayi==0:     #Eger sayi sifirsa faktoriyelinin 1 oldugunu belirtelim.
        return 1
    else:
        return sayi*faktoriyel(sayi-1) #Sonraki sayilar icin de 1'e kadar sayilarin carpimini tanimlayalim.
while True:
    sayi=int(input("Faktoriyel hesabi icin bir sayi giriniz: "))
    if sayi<1:
        print("\nLutfen 1'den buyuk bir sayi giriniz...\n")
    else:
        
        print(sayi,"sayisinin faktoriyeli: ",faktoriyel(sayi),"\n")     #input alip faktoriyelini yazdir.


###9.soru
#9-Kullanıcıdan bir input alan ve bu inputun içindeki büyük
#ve küçük harf sayılarının veren bir fonksiyon yazınız.
print("""
                      Harf Sayaci
            Icinde buyuk kucuk harf bulunan
            bir kelimede kac adet buyuk harf
            ve kac adet kucuk harf oldugunu
                   soyleyen programa

                     Hosgeldiniz!!!
                     
                     """)
def harf_uzunlugu(kelime):      #buyuk kucuk harfler icin 0'dan baslayarak birer arttırarak
    kucuk=0                     #kac adet kucuk buyuk harf oldugunu saymasi saglanir.
    buyuk=0
    for i in kelime:
        if i.isupper():
            buyuk+=1
        if i.islower():
            kucuk+=1
    print("Yazida {} adet buyuk harf,{} adet kucuk harf vardir".format(buyuk,kucuk))
while True:
    kelime=input("Bir kelime giriniz: ")
    if kelime=="":
        print("Lutfen bir kelime giriniz...\n")
        continue
    else:
        print(harf_uzunlugu(kelime))




###10.soru
##10-Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan
##ve sonrasında bu kelimeleri harf 
##sırasına göre dizip tekrar tire ile ayırıp output olarak
##veren bir fonksiyon yazınız. 
##örnek girdi: green-red-yellow-black-white örnek çıktı:
##black-green-red-white-yellow
print("""
                Harf Sirasina Gore Siralama:
            Kullanicidan alacagimiz "-" ile ayrilmis
        kelimeleri harf sirasina gore siralayip cikti
                        verecegiz...
            Dilediginiz kelimeleri arasina "-" koyarak
                      asagiya yaziniz...

                        Basarilar!!!
                        """)
            
def kelime_sirasi():
    kelime=input("Lutfen '-' ile ayrilmis kelimeler giriniz: ")
    kelimeler=kelime.split("-")
    kelimeler.sort()
    print(*kelimeler,sep="-")
while True:
    kelime=input("İslem yapmak icin 1'e cikmak icin 2'ye basiniz: ")
    if kelime=="2":
        print("Cikiliyor...\n")
        quit()
    if kelime=="1":
        print(kelime_sirasi())



###11.soru
#Verilen bir listenin içindeki özgün elemanları
#ayırıp yeni bir liste olarak veren bir fonksiyon yazınız.
#Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]
print("""
            Ayni Elemanlari Eleme Programi:
        Olusturdugumuz Listedeki ayni olan elemanlari
        tek elmana donusturerek yeni bir Liste olusturalim.
                ..................
                
        
""")
def ozgun_liste():
    originalliste=["Ali","Veli","49","50","Ali","50","49","Ali","Veli","49","Ali"]
    yeni_liste=[]
    print("Original Liste: ",originalliste)
    for i in originalliste:
        if i not in yeni_liste:
            yeni_liste.append(i)
    return yeni_liste
    
print("\n","Yeni Ozgun Listemiz: ",*ozgun_liste())





###12.soru
##12. Verilen inputların tersten de aynı olup olmadığını
##kontrol eden bir fonksiyon yazınız.
##örnek: madam, tacocat, utrecht sonuç: True, True, False
print("""
            Kelime KOntrol
    Verilen kelimelerin tersten de
    okunusunu kontrol eden programa

            Hosgeldiniz!!!
            
    """)
##def tersi(*args):
##    kelime_ters=""
##    sonliste=[]
##    for i in args:
##        for j in range(len(i)-1,-1,-1):
##            kelime_ters+=i[j]
##        print(kelime_ters)
##        if i==kelime_ters:
##            sonliste.append(True)
##            kelime_ters = ""
##
##        else:
##            sonliste.append(False)
##            kelime_ters = ""
##
##    return sonliste
def ters(kelime=input("Bir kelime yaziniz: ")):
    if kelime==kelime[::-1]:
        print("Olumlu. Kelime tersten de ayni sekilde yaziliyor:",kelime,"=",kelime)
    else:
        print("Olumsuz. Kelime tersten de ayni sekilde yazilmiyor")
ters()










