# Kullanicidan sayi alip EBOB hesaplama

sayi1 = int(input("Birinci sayi girin: "))
sayi2 = int(input("ikinci saiyi girin: "))
 
EBOB = 0
k = 0
 
if sayi1 < sayi2:                   # büyük sayıyı al
    k = sayi2
else:
    k = sayi1 
 
while k > 0:                        # EBOB hesaplama
    if sayi1 % k == 0 and sayi2 % k == 0:
        EBOB = k
        break                       # iki sayıyı birbirine böl, bölüm sıfır ise kır
    k = k - 1
 
print('OBEB({}, {}):'.format(sayi1, sayi2), EBOB)
