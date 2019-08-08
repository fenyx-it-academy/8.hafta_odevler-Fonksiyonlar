#verilen sayinin asal sayi olup olmadigini kontrol eden program.


def prime_number(number):
    int_number = []                         # bos bir liste olusturuyoruz
    for i in range(2,number):               # sayimizi, 2 den girdigimiz sayiya kadar olan sayilara bolen dongu yaziyoruz
            int_number += [i]                   #eger tam bolunuyorsa listeye ekliyoruz.
    if int_number!=[]:                      #eger liste bos degilse bu bir asal sayi degildir.
        print('This number is a not prime number...')
    else:                                   #eger liste bossa bu bir asal sayidir.
        print("This number is a prime number...")

prime_number(35)



