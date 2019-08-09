def bolenleri_bul(sayi):
    bolen_listesi = []
    for i in range(1, sayi + 1):
        if (sayi % i == 0):
            bolen_listesi.append(i)
    return bolen_listesi


while True:
    sayi = input("Bölenlerini bulmak istediğiniz sayıyı giriniz (Çıkmak için 'q'):")
    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        print(bolenleri_bul(sayi))