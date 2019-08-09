def okunus(sayi):
    k1 = {'1': 'bir',
          '2': 'iki',
          '3': 'uc',
          '4': 'dort',
          '5': 'bes',
          '6': 'alti',
          '7': 'yedi',
          '8': 'sekiz',
          '9': 'dokuz'}
    k2 = {'0': ' ',
          '1': 'on',
          '2': 'yirmi',
          '3': 'otuz',
          '4': 'kirk',
          '5': 'elli',
          '6': 'altmis',
          '7': 'yetmis',
          '8': 'seksen',
          '9': 'doksan', }
#sayilarimizin yazilisini sozluk olarak kaydettik
#fonksiyona girilecek sayiyi str ye cevirdikten
#sonra her basamagi hangi sozlukte aramasi gerektigini girdik

    sayi=str(sayi)

    print(k2[(sayi[0])],k1[(sayi[1])])
okunus(95)