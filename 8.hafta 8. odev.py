print('b.')
'''
8-Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.
'''

def faktoriyel(sayi):
    faktor=1                    # carpimlari 1 den baslattik
    for i in range(1,sayi+1):
        faktor *=i
    return f'{sayi}! = {faktor} '

sayi = int(input('bir sayi giriniz :'))
if sayi == 0 or sayi == 1:      # if ile 1 ve 0 durumunu kontrolettik
    print('faktoriyel 1 dir')
else:
    print(faktoriyel(sayi))     # foksiyonumuzu cagirdik