def tam_bölenler(sayı):

    for i in range(1,sayı+1):
        if sayı%i == 0:
            print(i)

sayı = int(input("bir sayı giriniz"))
tam_bölenler(sayı)
