print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")


def perfect(number):
    toplam = 0                              #tam bolenlerinin toplami icin sayac
    for tam in range(1, number):
        if(number % tam == 0):
            toplam += tam                   #her tam bolen buldugunda toplasin diye
    if(toplam == number):
        return True


perfect_number = []                               #mukemmel sayilar listesi olusturduk
for i in range(1, 1000):
    if perfect(i):                                #mukemmel sayi fonksiyonunu kullanarak sayi var ise
        perfect_number.append(i)                  #mukemmel sayi var ise listeye ekle
print(f"Perfect numbers are between 1 and 1000: {perfect_number}")

