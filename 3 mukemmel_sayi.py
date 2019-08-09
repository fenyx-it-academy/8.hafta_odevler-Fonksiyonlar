def mukemmel(sayi):
    adet = 0;
    for i in range(1, sayi):
        if sayi % i == 0:
            adet += i
    if adet == sayi:
        print(sayi, " mukemmel sayidir.")
    else:
        print(sayi, " mukemmel sayi degil")
        return
for i in range (1000):
    number=mukemmel(i)
    print(number)
