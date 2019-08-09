# coding=utf-8
def faktoriyel(sayı):
    #fonksiyon ve parametre tanımlama
    try:
        carpım=1
        #carpımın tutulacagı degisken
        for i in range(2,sayı+1):
            #2den sayıya kadar dongu
            carpım*=i
            #carpım degiskenini dongudeki sayı ile carpma
        return print(f'{sayı}! =',carpım)
        #return ile sonucu ekrana yazdırma

    except:
        #hatalı giris uyarısı
        return print('Lütfen bir tamsayı girdiğinizden emin olunuz.')



