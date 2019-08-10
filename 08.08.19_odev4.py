def ebob():                                                     # fonksiyonumuzu adlandirdik
    x = int(input("Lutfen 1. sayiyi giriniz : "))               # verileri aldik
    y = int(input("Lutfen 2. sayiyi giriniz : "))

    list_x = []                                                 # 3 tane bos liste olusturduk
    list_y = []
    com_list = []
    for i in range(1, x + 1):                                   # 2 farkli dongu ile listeleri olusturduk
        if x % i == 0:
            list_x.append(i)

    for i in range(1, y + 1):
        if y % i == 0:
            list_y.append(i)

    if len(list_x) < len(list_y):                               # 2 farkli if formulasyonu ile sonuca ulastik
        for i in list_y:
            if i in list_x:
                com_list.append(i)
                com_list.reverse()


    if len(list_x) > len(list_y):
        for i in list_x:
            if i in list_y:
                com_list.append(i)
                com_list.reverse()

    return com_list[0]                                      # sonucu verdik

print(ebob())                                               # fonksiyomuzu cagirdik