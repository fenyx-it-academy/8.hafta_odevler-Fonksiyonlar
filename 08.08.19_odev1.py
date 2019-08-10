def asal():                                                                     # fonksiyonumuzu adlandirdik
    sayi=int(input("Lutfen kontrol etmek istediginiz sayiyi giriniz : "))       # kullanicidan sayi aldik
    if sayi == 1:                                                               # 3 asamali asal sayi kontrollerini yaptik ve sonuclarini return ile verdik
        return "Asal sayi degil"
    elif sayi == 2:
        return "Asal sayi"
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                return "Asal sayi degil"
        return "Asal sayi"

print(asal())                                                                   # fonksiyonumuzu cagirdik