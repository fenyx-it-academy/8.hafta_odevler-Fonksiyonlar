def terskontrol(*kelime):
    for i in kelime:
        for c in i:
            if c==c[::-1]:
                return print("True")

            else:
                return False


while True:
    a = input("KElimeyi Giriniz : ")

    print(terskontrol(a))

