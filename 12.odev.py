def ters():
    while True:
        deger=input("lutfen bir deger giriniz")
        if deger==deger[::-1]:
            print("True")
        else:
            print("False")
        cevap=input("Denemey devam etmek istiyormusunuz: E/H")
        if cevap=="E":
            continue
        elif cevap=="H":
            quit()
        else:
            print("yanlis bir secim yaptiniz")
            quit()

ters()