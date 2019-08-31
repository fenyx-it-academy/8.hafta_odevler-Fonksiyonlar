sayi1 = int(input("Bir sayi girin: "))
sayi2 = int(input("ikinci saiyi girin: "))
 
EKOK=0
k = 0
 
if sayi1 < sayi2:                   # büyük sayıyı al
    k = sayi2
else:
    k = sayi1 
 
while k <= sayi1 * sayi2:            # EKOK hesaplama
    if k % sayi1 == 0 and k % sayi2 == 0:
         OKEK = k
         break                      # iki sayıyı çarp birbirlerine bölümü tam ise kır
    k = k +1
 
print('OKEK({}, {}):'.format(sayi1, sayi2), EKOK)
