print('b.')

'''4-Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.'''

def ebob_bul(sayi1,sayi2):
    birinci_sayi_bolenleri = []
    ikinci_sayi_bolenleri = []
    # birinci sayinin bolenlerini bulduk
    for birBol in range(1, sayi1 + 1):
        if sayi1 % birBol == 0:
            birinci_sayi_bolenleri.append(birBol)
    # ikinci sayi bolenlerini bulduk
    for ikiBol in range(1, sayi2 + 1):
        if sayi2 % ikiBol == 0:
            ikinci_sayi_bolenleri.append(ikiBol)
    # kumeye cevirip iki sayinin bolenlerinin kesisimini bulduk
    bolenlerin_kesisimi = set(birinci_sayi_bolenleri) & set(ikinci_sayi_bolenleri)
    print(max(bolenlerin_kesisimi))  # bolenlerin kesimindden en buyuk sayiyi bulduk
#input aldik
sayi1=int(input('1.sayiyi giriniz'))
sayi2=int(input('2.sayiyi giriniz'))
ebob_bul(sayi1,sayi2)               # fonks cagiriyoruz