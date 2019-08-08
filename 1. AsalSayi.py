
#sadece bir tane parametre gonderebilecegimiz bir fonksiyon tanimladik

def asalSayiMi(sayi):
    if sayi == 1:
        #Eger 1 degeri girilirse asal olmadigi icin false doner
        return False
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                #2 den baslayarak her sayiyi girilen sayiya boleriz.
                # Eger tam bolunen bir sayi olursa o sayi asal degildir o yuzden false doner
                return False
        #diger tum sayilar asal olacagi icin true doner
        return True

try:
    while True:
        sayi = input("Asal olup olmadigini merak ettiginiz bir sayi girin: ")
        if sayi == "q":
            print("Program Sonlandiriliyor...")
            break
        elif sayi.isdigit() == True:
            #girilen deger eger rakamlardan olusuyorsa asagidaki islemler yapilir
            # input string oldugu icin inte cevirdik
            sayi = int(sayi)
            if asalSayiMi(sayi) == True:
                print("{} sayisi asal sayidir".format(sayi))
            else:
                print("{} sayisi asal sayi degildir".format(sayi))
        else:
            print('Hatali giris yaptiniz. Lutfen sayi girin!')
except:
    print('Hatali islem. Program sonlandirildi..')