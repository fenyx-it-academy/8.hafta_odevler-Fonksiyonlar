#bu kod bir sayinin faktoriyelini bulur

def faktoriyel(sayi):               #faktoriyel bulma fonksiyonunun adini belirler
    faktryl=1                       #faktoriyel islemi icin carpmaya 1 ile baslanir.0!=1 dir.
    for i in range(1,sayi+1):       #1 den verilen sayiya kadar olan butun sayilari ele alir
        faktryl*=i                  #her gelen yeni sayiyi faktryl sonucuyla carparak butun sayilari carpar.
    return faktryl                  #carpim sonucunu geri dondurur


while True:
    sayi=input("faktoriyelini bulmak icin bir sayi giriniz(cikis icin q)")     #faktoriyelini bulmak istedigi sayi sorar

    if sayi=="q":                                                   #cikis yapmak isteyenler icin cikis blogu
        break

    elif sayi.startwith()=="-":                             #kullanici negatif input verirse uyari verir
        print("negatif sayi girmeyiniz")

    elif sayi.idigit()==False:                              #kullanici sayi haricinde bir input girerse uyari verir
        print("bir sayi degeri giriniz")

    else:                                                   #islem sonucunun basildigi kisim
        sayi1=int(sayi)
        sonuc=faktoriyel(sayi1)                         #kullanicinin girdigi sayinin faktoriyelini alir
        print(f"""                                      
{sayi}!={sonuc}
{sayi} faktoriyelin sonucu {sonuc} dur.""")             #sonucu printler