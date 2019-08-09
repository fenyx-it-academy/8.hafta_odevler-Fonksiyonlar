""""Sayi Okunusu"""
def sayiokunusu(sayi):
    #sayilarin yazi ile karsiligini sozlukte tablo degiskeni ile atadik
    tablo = { 0 : 'sifir', 1 : 'bir', 2 : 'iki', 3 : 'uc', 4 : 'dort', 5 : 'bes',
          6 : 'alti', 7 : 'yedi', 8 : 'sekiz', 9 : 'dokuz', 10 : 'on',
          11 : 'on bir', 12 : 'on iki', 13 : 'on uc', 14 : 'on dort',
          15 : 'on bes', 16 : 'on alti', 17 : 'on yedi', 18 : 'on sekiz',
          19 : 'on dokuz', 20 : 'yirmi',
          30 : 'otuz', 40 : 'kirk', 50 : 'elli', 60 : 'altmis',
          70 : 'yetmis', 80 : 'seksen', 90 : 'doksan' }
    if sayi < 20:#sayimiz yirmiden kucuk ise sayimizin valuesini yazdiriyoruz
        return tablo[sayi]

    else:
        if sayi % 10 == 0:#saymiz onun kati ise valuesini yazdiriyoruz
            return tablo[sayi]
        else:#sayimiz 20 den buyukse birinci basamagini yuze bulup yuvarliyoruz
            #ikinci basamgini ise ondan bolumunden kalani yazip strin olarak birlestiriyoruz
            return tablo[sayi // 10 * 10] + '-' + tablo[sayi % 10]
while True:
    try:
        sayi = int(input("iki basamakli bir sayi girin"))
        print(sayiokunusu(sayi))
    except:#sayi disinda farkli bir degerde uyari ver
        print("bir hata olustu")