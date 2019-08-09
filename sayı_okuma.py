# # coding=utf-8

def sayı_okuma(sayı):
    #fonksiyon ve paremetre tanımlama
    birler = {
        0: '',
        1: 'bir',
        2: 'iki',
        3: 'üç',
        4: 'dört',
        5: 'beş',
        6: 'altı',
        7: 'yedi',
        8: 'sekiz',
        9: 'dokuz',
    }
    onlar = {
        0: '',
        1: 'on',
        2: 'yirmi',
        3: 'otuz',
        4: 'kırk',
        5: 'elli',
        6: 'altmış',
        7: 'yetmiş',
        8: 'seksen',
        9: 'doksan',
    }
    #sözlük tanımlama
    try:
        sayi_liste=list(str(sayı))
        #sayıyı stringe çevirip rakamları ile liste olusturma
        return print(f'{sayı} =',onlar[int(sayi_liste[0])]+' '+birler[int(sayi_liste[1])])
        #return ile sayının okunusunu ekrana yazdırma
    except:
        #hatalı giris uyarısı
        return print('İki basmaklı bir sayı girdiğinizden emin olunuz.')


