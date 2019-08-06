##Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir
##fonksiyon yazın. Örnek: 97 ---------> Doksan Yedi
while True:
    def oku(a):
        if liste[0]=="1":
            sayi="On"
        if liste[0]=="2":
            sayi="Yirmi"
        if liste[0]=="3":
            sayi="Otuz"
        if liste[0]=="4":
            sayi="Kirk"
        if liste[0]=="5":
            sayi="Elli"
        if liste[0]=="6":
            sayi="Altmis"
        if liste[0]=="7":
            sayi="Yetmis"
        if liste[0]=="8":
            sayi="Seksen"
        if liste[0]=="9":
            sayi="Doksan"
            
        if liste[1]=="0":
            sayi1=""
        if liste[1]=="1":
            sayi1="bir"
        if liste[1]=="2":
            sayi1="iki"
        if liste[1]=="3":
            sayi1="uc"
        if liste[1]=="4":
            sayi1="dort"
        if liste[1]=="5":
            sayi1="bes"
        if liste[1]=="6":
            sayi1="alti"
        if liste[1]=="7":
            sayi1="yedi"
        if liste[1]=="8":
            sayi1="sekiz"
        if liste[1]=="9":
            sayi1="dokuz"

        return "Sayiniz: " +sayi+" " +sayi1
    rakam=input("Iki basamakli bir sayi giriniz cikis icin 'q':").lower()
    if rakam=='q':
        break
    if int(rakam)<10 or int(rakam)>99:
        print("Lutfen iki basamakli bir sayi giriniz!","\n")
    else:
        liste=[]
        for i in rakam:
            liste+=[i]
        print(oku(rakam),"\n")
        
        
        
