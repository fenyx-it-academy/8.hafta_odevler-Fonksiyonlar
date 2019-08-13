def tambol():                                                                           # fonksiyonumuzu adlandirdik
    sayi=int(input("Lutfen tam bolenlerini bulmak istediginiz sayiyi giriniz : "))      # kullanicidan sayi aldik

    list = []                                                                           # bos liste olusturduk
    for i in range(1, sayi+1):                                                          # dongu ile formulasyonumuzu yaptik
        if sayi%i==0:
            list.append(i)
    return list                                                                         # return ile sonucumuzu verdik

print(tambol())                                                                         # fonksiyonumuzu cagirdik