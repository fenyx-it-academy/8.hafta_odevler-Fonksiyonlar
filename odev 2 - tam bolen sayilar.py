#bir sayinin tam bolenlerini
def divider(number):
    """bir sayinin tam bolenlerini bulan fonksiyon"""
    int_number = []                     # bos bir liste tanimliyoruz
    for i in range(1,number+1):         # 1 den girdigimiz sayiyida icine alacak sekilde range() dongusu kuruyoruz.
        if number % i == 0:             # eger sayimiz dongudeki sayiya tam bolunuyorsa
            int_number += [i]           # listeye ekle
    print("{} sayisini tam bolen sayilarin kumesi {} dir.".format(number,int_number))

divider(36)