"""tam bolen bulma"""
def tambolenler(sayi):
    tam_bolen =[]
    for i in range(2,sayi):#iki ile girdigimiz sayi arasinda dongu olusturduk
        if sayi % i == 0:#sayi dongudeki sayilara tam tam bolunuyorsa  tam_bolen =[] listesine ekle
            tam_bolen.append(i)
    return tam_bolen

while True:#inputu surekli almamiz icin dongu olusturduk
    try:
        sayi = int(input("bir sayi girin: "))
        if sayi:#sayi girisi yapilmissa
            print("tam bolenlerimiz",tambolenler(sayi))
    except:#int() disinda farkli bir giris yapilirsa islem yapma kullaniciya uyar
        print("hatali giris")