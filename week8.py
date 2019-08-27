##.Hafta Ödevler
##Asal sayi olup olmadigini kontrol eden fonksiyon yazınız.

def asal(sayi):  
  if sayi==1:
    return "Asal degil"
  if sayi==2:
    return "Asal"            # asal adinda sayi parametresi olan bir fonksiyon tanimladik.
  for i in range(2,sayi-1): #Kendisinden baska bir sayi ile bolunup bolunmedigini kontrol etmek icin 2den sayinin 1 eksigine kadar-
    if sayi%i==0:           # tum sayilarla bolumunden kalan 0 ise:
      return "Asal degil"   #Asal degil olarak dondur.
    else:                   # degilse
      return "Asal sayi"    # Asal sayi stringini dondur.
sayi=2
print(sayi, "nin asallik durumu: ",asal(sayi))    # Fonksiyonu 10 argumani ile dondurduk.

##Bir sayinin tam bolenlerini bulan fonksiyon yazınız.

def tambolen(sayi):             # Adi tambolen sayi isminde bir parametresi olan fonksiyon olusturduk.
  liste=[]                      # Tam bolunen sayilari atmak icin liste olusturduk.
  for i in range(1,sayi-1):     # Sayinin 1 eksigine kadar tum sayilari donduruyoruz.
    if sayi%i==0:               # Eger bu sayilardan herhangi biri ile bolumunden kalan 0 ise:
      liste.append(i)           # Listeye append metodu ile ekliyoruz.
    continue                    # Degilse devam et.
  return liste                  # Listeyi dondur

print("Tam bolenleri: ",tambolen(40))  # Fonksiyonu calistirip sonucunu printledik.


##1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
#Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

def mukemmel(sayi):             # Mukemmel adinda sayi adinda bir parametresi olan fonksiyon tanimladik. 
  toplam=0                      # Sayinin bolenlerinin toplami toplam adinda integer tanimladik. 
  for i in range(1,sayi-1):     # Sayinin 1 eksigi kadar donguyu kurduk.
    if sayi%i==0:               # Sayinin boleni olup olmadigi kontrolu yapiyoruz.
      toplam+=i                 # Bolumunden kalan 0 ise toplama sayiyi ekliyor.
    continue                    # Degilse devam et 
  if toplam==sayi:              # Eger bolenlerin toplami ile sayimiz esitse:
    return True                 # True degerinin dondurduk 

print("Mukemmel Sayilar")       
for i in range(101):            # 1 den 100 kadar tum sayilari donduruyoruz.
  if mukemmel(i):               # Fonksiyonumuzu cagirip sayilarin kontrolunu yapiyoruz. True ise:
    print(i)                    # Printliyoruz



##Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

def ebob():                          # ebob adinda bir fonksiyon tanimladik.
  a=int(input("Birinci Sayi: "))     # Kullanicidan sayi aliyoruz
  b=int(input("Ikinci Sayi: ")) 
  carp=[]                            # Bolen sayilarin degerlerini aldigimiz bos bir liste tanimladik
  for i in range(2,min(a,b)):        # 2den sayilarin kucugune kadar olan sayilari donduruyoruz.
    if a%i==0 and b%i==0:            # Eger her iki sayi dondurdugumuz sayilarla tam bolunuyorsa:
      carp.append(i)                 # carp listemize sayiyi ekle.
    continue                         # Degilse devam et.
  return max(carp)                   # Listenin icindeki en buyuk bolen ebob oldugu icin onu donduruyoruz.

print("Ebob",ebob())                 # Fonksiyonumuzu calistirip printledik.
    
##Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

def ekok():                             # ekok adinda bir fonksiyon tanimladik. 
  a=int(input("Birinci Sayi: "))        # Kullanicidan sayi aliyoruz
  b=int(input("Ikinci Sayi: "))                                   
  carp=0                                # carp adinda ekoku buldugumuzda bu degeri tutacak bir integer tipinde degisken tanimladik.
  for i in range(2,min(a,b)):           # 2den sayilarin en kucugune kadar degerleri donduruyoruz 
    if (a*i)%a==0 and (a*i)%b==0:       # Eger dondurdugumuz sayilar ile her iki sayinin carpiminin kalani 0 ise:
      carp=a*i                          # En kucuk ortak kati bulmus oluyoruz. carp degiskenine atiyoruz.
      break                             # Aradigimiz degeri buldugumuz icin break ile donguden cikiyoruz.
  return carp                           # carp degiskenini fonksiyon sonucu olarak donduruyoruz.

print("Ekok",ekok())                    # Fonksiyonumuzu calistirip donduruyoruz.
    

##Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın. Örnek: 97 ---------> Doksan Yedi

def Okunus():              # Okunus adinda bir fonksiyon tanimladik.            
  sayi=input("Sayi: ")     # Kullanicidan sayi aliyoruz
  bir={"0":" ","1":"bir","2":"iki","3":"uc","4":"dort","5":"bes","6":"alti","7":"yedi","8":"sekiz","9":"dokuz"}              # Birler basamasigi icin 1 sozluk
  iki={"0":" ","1":"On","2":"Yirmi","3":"Otuz","4":"Kirk","5":"Elli","6":"Altmis","7":"Yetmis","8":"Seksen","9":"Doksan"}    # Onlar basamagi icin 1 sozluk olusturduk
  print(iki[sayi[1]],bir[sayi[0]])                                                                                          # Sayinin 0 ve 1.indexlerine gore okunuslari yazdirdik

Okunus()



##1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisagor(sayi):                             # pisagor adinda tek parametreli fonksiyon olusturduk.               
  for a in range(sayi):                        # sayiya kadar don 
    for b in range(1, a):                      # ic ice 1den baslayarak diger sayinin alt elemanlarini don 
        c = ( a * a + b * b)**0.5              # c2= a2+b2 pisagor formulunu yazdik 
        if c % 1 == 0:                         # eger c degeri 1 ile bolumunden kalan 0 ise yani tamsayi ise:
            print(b, a, int(c))                # ucgeni saglayan degerleri yazdir 
            
pisagor(100)                                   # 100 argumant ile pisagor fonksiyonunu calistirdik 


##Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.

def fak(sayi):                        # fak adinda sayi parametreli fonksiyon tanimladik.
  fakt=1                              # sayilarin carpimi icin fakt integer degisken tanimladik.
  for i in range(1,sayi+1):           # 1den sayiya kadar tum sayilari donduruyoruz.
    fakt*=i                           # fakt degiskeni ile her sayiyi carpiyoruz.
  return fakt                         # bu degiskeni sonuc olarak donduruyoruz.

print("Faktoriyeli: ",fak(3))         # fonksiyonu calistirip donduruyoruz.



##Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf sayılarının veren bir fonksiyon yazınız.

def kucukbuyuk():                    # kucukbuyuk adinda bir fonksiyon olusturduk.
  giris=input("Giris yapiniz: ")     # Kullanicidan giris yapmasini istedik
  buyuk=0                            # buyuk ve kucuk adinda integer veriler tanimladik harfleri saymak icin.
  kucuk=0
  for i in giris:                    # girisin tum harflerini kontrol etmek icin donduruyoruz.
    if i.isupper():                  # isupper fonksiyonu ile buyuk harf oluo olmadigini kontrol ettik.
      buyuk+=1                       # Oyleyse buyuk 1 ekledik.
    elif i.islower():                # islower ile kucuk harf olup olmadigini kontrol ettik.
      kucuk+=1                       # Oyleyse kucuk 1 arttir.
  return kucuk,buyuk                 # kucuk buyuk degerlerini dondurduk 

print("Kucuk Buyuk Harf: ",kucukbuyuk())    

##Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve sonrasında bu kelimeleri harf sırasına göre
#dizip tekrar tire ile ayırıp output olarak veren bir fonksiyon yazınız.
#örnek girdi: green-red-yellow-black-white örnek çıktı: black-green-red-white-yellow

def ters():                                       # ters adinda girdi parametreli bir fonksiyon olusturduk.
  girdi=input("Giris yapiniz: ")                  # Kulanicidan veri aldik                                       
  girdi=girdi.split("-")                          # girdi stringini split metodu ile - isaretlerinden bolup liste olusturduk.
  girdi.sort()                                    # sort metodu ile listeyi siraladik.
  print(*girdi,sep="-")                           # girdinin son halini sep ile aralarina - koyarak yazdirdik  
ters()
  

##Verilen bir listenin içindeki özgün elemanları ayırıp yeni bir liste olarak veren bir fonksiyon yazınız. Örnek Liste : [1,2,3,3,3,3,4,5,5] Özgün Liste : [1, 2, 3, 4, 5]

def ozgun(liste):                      # ozgun adinda liste parametresi olan bir fonksiyon olusturduk.
  a=set(liste)                         # set ile kumeye donusturduk listeyi eleman fazlaligindan kurtulmak icin.
  a=list(a)                            # Tekrar listeye cevirip-
  return a                             # a listesini donduruyoruz 

print(ozgun([1,2,3,3,3,3,4,5,5]))



##Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız. örnek: madam, taco cat, utrecht sonuç: True, True, False



def fonk(*args):                                # fonk adinda birdan fazla argumant olabilen fonksiyon olusturduk
  durum=" "                                     # durumlari atmak icin string tanimladik.
  for i in args:                                # args tuple uzerinde degerlerini donduruyoruz.
    if i== i[::-1]:                             # eger deger ile tersi esitse duruma True ekliyoruz.
       durum+="True"
    else:                                       # degilse duruma False ekliyoruz.
      durum+="False"
  return durum                                  # durumu donduruyoruz.
    
print(fonk("madam","tacocat","utrecht"))





