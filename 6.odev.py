'''
6-Kullanıcıdan 2 basamaklı bir sayı alın
 ve bu sayının okunuşunu bulan bir fonksiyon yazın.
  Örnek: 97 ---------> Doksan Yedi
'''

def sayı_okunuş(sayı):
    # sayıların okunuşlarını sözlüklere tanımlıyoruz
    birler_basamağı ={
            '0':'',
            '1':'bir',
            '2':'iki',
            '3':'üç',
            '4':'dört',
            '5':'beş',
            '6':'altı',
            '7':'yedi',
            '8':'sekiz',
            '9':'dokuz'}
    onlar_basamağı={
            '1':'on',
            '2':'yirmi',
            '3':'otuz',
            '4':'kırk',
            '5':'elli',
            '6':'altmış',
            '7':'yetmiş',
            '8':'seksen',
            '9':'doksan'}
    onlarB = onlar_basamağı[sayı[0]]
    birlerB = birler_basamağı[sayı[1]]
    return f'{sayı} -----------> : {onlarB} {birlerB}'

sayı = input('bir sayı giriniz :')        # kullanıcıdan input ile sayımızı aldık
print(sayı_okunuş(sayı))
