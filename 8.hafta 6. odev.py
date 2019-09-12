print('b.')
'''
6-Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
Örnek: 97 ---------> Doksan Yedi
'''
def sayi_okunus(sayi):
    # sayilari okunuslarini sozluklere tanimladik
    birler_basamagi={
            '0':'',
            '1':'bir',
            '2':'iki',
            '3':'uc',
            '4':'dort',
            '5':'bes',
            '6':'alti',
            '7':'yedi',
            '8':'sekiz',
            '9':'dokuz'}
    onlar_basamagi={
            '1':'on',
            '2':'yirmi',
            '3':'otuz',
            '4':'kirk',
            '5':'elli',
            '6':'altmis',
            '7':'yetmis',
            '8':'seksen',
            '9':'doksan'}
    #girilen sayinin basamaklarini kontrol ettik ve sozlukten karsiliklarini bulduk
    onlarB = onlar_basamagi[sayi[0]]
    birlerB =birler_basamagi[sayi[1]]
    return f'{sayi} -----------> : {onlarB} {birlerB}'

sayi=input('bir sayi giriniz :')        # kullanicidan input ile sayimizi aldik
print(sayi_okunus(sayi))