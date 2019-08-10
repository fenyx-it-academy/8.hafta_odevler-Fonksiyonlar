def buy_kuc():                                                              # fonksiyonumuzu adlandirdik
    kucuk = "abcdefghijklmnopqrstuvwxyz"                                    # alinan veriyi kontrol edecek mekanizmayi olusturduk
    buyuk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    kucuk_list = []                                                         # 2 bos liste olusturduk
    buyuk_list = []

    metin = input("Lutfen metninizi giriniz : ")                            # kullanicidan veri aldik

    for i in metin:                                                         # sonuca goturecek dongumuzu kurduk
        if i in kucuk:
            kucuk_list.append(i)

        elif i in buyuk:
            buyuk_list.append(i)

    return (len(metin), len(kucuk_list), len(buyuk_list))                   # sonucu verdik

print(buy_kuc())                                                            # fonksiyonumuzu cagirdik