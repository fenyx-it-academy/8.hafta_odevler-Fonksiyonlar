'''
Kullanıcıdan 2 tane sayı alarak
 bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
'''

def ekok(sayi1, sayi2):
    if sayi1 > sayi2:
        ekok = sayi1
    else:
        ekok = sayi2
    while (True):
        if ((ekok % sayi1 == 0) and (ekok % sayi2 == 0)):
            break
        ekok += 1
    return f'{sayi1} ve {sayi2} ekok u : {ekok}'
sayi1=int(input('1.sayiyi giriniz'))
sayi2=int(input('2.sayiyi giriniz'))
print(ekok(sayi1,sayi2))
