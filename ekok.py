# coding=utf-8
def ekok(sayı1,sayı2):
    #fonksiyon ve iki parametresinin tanımlanması
    try:
        for i in range(abs(sayı1),0,-1):
            #sayı1 in mutlak degerinden 1 e kadar azalan dongü
            if sayı1%i==0 and sayı2%i==0:
                #dongudeki sayı iki sayıyıda boluyorsa bu sayı ebob'u verir
                return print(f'EKOK({sayı1},{sayı2}) =',int((sayı1*sayı2)/i))
                #sayı1 ve sayı2 nin capımının ebob'a bolumu ekok'u verir
    except:
        #hatalı giris uyarısı
        return print('Lütfen giridiğiniz verilerin tamsayı olduğundan emin olunuz.')

