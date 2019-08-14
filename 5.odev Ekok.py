##Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak
##katlarını (EKOK) dönen bir tane fonksiyon yazın.

#ortak kat bulunacagi icin bir ust rakam belirledik. orn=100-100
def ekok(sayi1,sayi2):
    sayac1 = 100
    sayac2 = 100
    BolunebilenListe1 = []
    BolunebilenListe2 = []
    OrtakListe = []
    for i in range(sayi1,sayac1):
        if i % sayi1 == 0:
            BolunebilenListe1 += [str(i)]
            sayac1 -= 1      
    print("BolunebilenListe1 : ", BolunebilenListe1)
    for k in range(sayi2,sayac2):
        if k % sayi2 == 0:
            BolunebilenListe2 += [str(k)]
            sayac2 -= 1
    print("BolunebilenListe2 : ", BolunebilenListe2)
    for m in BolunebilenListe1:
        if m in BolunebilenListe2:
            OrtakListe += [m]
    print("Ekok Liste : ", OrtakListe)
    print("Ekok : ",OrtakListe[0])
    return BolunebilenListe1
    return BolunebilenListe2 
    return OrtakListe             
ekok(int(input("Bir sayi giriniz : ")),int(input("Baska bir sayi giriniz : ")))
