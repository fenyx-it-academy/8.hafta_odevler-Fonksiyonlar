""""bir sayinin asal olup olmadigini  bulma"""
def asal_mi(sayi):#fonksiyonumuzda alacagimiz sayi asal ise True degilse False degeri donecek
    if sayi == 1:#asal olmadigi icin False donecek
        return False
    elif sayi == 2:#asal oldugu icin True donecek
        return True
    else:#girdigimiz sayi 1 ve 2 nin disinda ise
        for i in range(2,sayi):#iki ile girdigimiz sayi arasinda dongu olusturduk
            if sayi % i == 0:#donguden cikan sayi asal ise True degilse False
                return False
            else:
                return True
while True:#inputu surekli almamiz icin dongu olusturduk
    try:
        sayi =  int(input("sayinizi giriniz: "))
        if asal_mi(sayi):#sayi True ise
            print("{} sayisi asal sayidir".format(sayi))
        else:#sayi False ise
            print("{} sayisi asal sayi degildir".format(sayi))
    except:#int() disinda farkli bir giris yapilirsa islem yapma kullaniciya uyar
        print("hatali giris")