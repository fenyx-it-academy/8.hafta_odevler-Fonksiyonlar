# coding=utf-8
def asal_sayı(sayı): # fonksiyon tanımlama
    try:
        sayı=int(sayı) # girilen veriyi int.e dönüştürme
        kontrol=round(sayı**0.5)+1 #verilen sayının karekökün yaklasık degerinin 1 fazlası alınıyor.

        if sayı!=2 and sayı%2==0 or sayı<2: # 2 den farklı 2 ye bolunuyorsa veya 2 den kucukse sayı asal degil
            return print(f'{sayı} asal sayı degil') #fonksiyondan asal sayı degil cıktısı return yapma

        for i in range(3,kontrol,2): #3 den kontrol sayısına kadar tek sayılar icin dongu
            if sayı%i==0: #verilen sayının yukarıda belirtilen sayılara bolunup-bolunmedigini kontrol
                return print(f'{sayı} asal sayı degil')

        else: #yukardaki kosullu durumları saglamadıysa sayı asaldır
            return print(f'{sayı} asal sayı ')

    except ValueError: # hatalı veri girisinde uyarı mesajı yazdırma
        print('Tamsayı gimediniz. Tekrar deneyiniz.')




