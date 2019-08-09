# coding=utf-8
def ebob(sayı1,sayı2):
    #fonksiyon ve iki parametre tanımlama
    try:
        for i in range(abs(sayı1),0,-1):
            #sayı1 in mutlak degeri ust sınır olacak sekilde 1 e kadar geriye dogru dongu
            if sayı1%i==0 and sayı2%i==0:
                #dongudeki sayı iki sayıyıda tam boluyorsa
                return print(f'EBOB({sayı1},{sayı2}) =',i)
                #return ile ekrana sayıların ebobini yazdırma
    except:
        #hatalı giris uyarısı
        return print('Lütden girdiğiniz verilerin tamsayı olduğundan emin olunuz')



