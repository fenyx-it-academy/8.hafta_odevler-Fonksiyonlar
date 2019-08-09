def sayiokunus(x):
    okunus1={0:"sifir",1:"On",2:"Yirmi",3:"Otuz",4:"Kirk",5:"Elli",6:"Altmis",7:"Yetmis",8:"Seksen",9:"Doksan"}
    okunus2={0:"",1:"bir",2:"iki",3:"Uc",4:"dort",5:"bes",6:"Alti",7:"Yedi",8:"Sekiz",9:"Dokuz"}
    bos = []
    if len(x) != 2:
        print("Lutfen iki basamkli bir sayi giriniz")
    for i in x:
        bos.append(i)
    print(x, "=", okunus1[int(bos[0])], okunus2[int(bos[1])])


while True:
    print("Cikmak Icin 'q'ya basiniz")
    try:
        sayi = input("Okunusunu merak ettiginiz iki basamakli bir sayiyi giriniz:")
        if sayi == 'q' or sayi == 'Q':
            print("Cikiliyor...")
            break
    except ValueError:
        print("lutfen sayisal deger giriniz")
    sayiokunus(sayi)



