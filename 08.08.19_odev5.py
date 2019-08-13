def ekok():                                                 # fonksiyonumuzu adlandirdik
    x = int(input("Lutfen 1. sayiyi giriniz : "))           # kullanicidan verileri aldik
    y = int(input("Lutfen 2. sayiyi giriniz : "))

    list_x = []                                             # 3 bos liste olusturduk
    list_y = []
    com_list = []

    for i in range(1, 100):                                 # 3 ayri for dongusu ile listeleri doldurduk
        list_x.append(x * i)

    for i in range(1, 100):
        list_y.append(y * i)

    for i in list_y:
        if i in list_x:
            com_list.append(i)

    return com_list[0]                                      # sonucu verdik

print(ekok())                                               # fonksiyonumuzu cagirdik