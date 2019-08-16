#bu kod 100e kadar olan tam sayilardan pisagor bagintisini saglayanlari bulur.

def hip(sayi1,sayi2):                       #hipotenus hesaplama fonksiyonunun adi
    hipotenus=(sayi1**2+sayi2**2)**0.5      #iki kenarin kareleri toplaminin karekoku=hipotenusdur
    return hipotenus                        #hipotenusu geri dondur




for a in range(1,100):                          #birinci kenar uzunlugu 100 e kadar olan tamsayilardan olsun
    for b in range(1,100):                      #ikinci kenar uzunlugu 100 e kadar olan tamsayilardan olsun

        if hip(a,b)<=100 and hip(a,b).is_integer():            #hipotenus 100 den kucuk ve tamsayi olma durumu
            print(f"{a},{b} iki dik kenar olmak uzere hipotenus {hip(a,b)} dir.")       #bu uc kenari printle

        else:
            pass

