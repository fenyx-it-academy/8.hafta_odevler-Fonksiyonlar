##4. Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak
##bölenini (EBOB) dönen bir tane fonksiyon yazın.
#### Not: listeye (str) oge eklemek istiyorsak [] icine almamiz gerekir. integer icin gerek yok

def ebob(sayi1,sayi2):
    sayac1 = 1
    sayac2 = 1
    BolunebilenListe1 = []
    BolunebilenListe2 = []
    OrtakListe = []
    for i in range(sayac1,(sayi1+1)):
        if sayi1 % i == 0:
            BolunebilenListe1 += [str(i)]
            sayac1 += 1      
    print("BolunebilenListe1 : ", BolunebilenListe1)
    for k in range(sayac2,(sayi2+1)):
        if sayi2 % k == 0:
            BolunebilenListe2 += [str(k)]
            sayac2 += 1
    print("BolunebilenListe2 : ", BolunebilenListe2)
    for m in BolunebilenListe1:
        if m in BolunebilenListe2:
            OrtakListe += [m]
            OrtakListe.sort()
    print("Ebob : ", OrtakListe)
    print("Ebob : ", OrtakListe[-1])
#return leri her for dongusunun arasina yazarsak sadece ilk donguyu calistiriyor!!
    return BolunebilenListe1
    return BolunebilenListe2 
    return OrtakListe        
ebob(int(input("Bir sayi giriniz : ")),int(input("Baska bir sayi giriniz : ")))
