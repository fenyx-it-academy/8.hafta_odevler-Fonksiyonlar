print('b.')

'''
10-Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve 
sonrasında bu kelimeleri harf sırasına göre dizip tekrar tire ile ayırıp
output olarak veren bir fonksiyon yazınız. örnek girdi: green-red-yellow-black-white 
örnek çıktı: black-green-red-white-yellow'''

def siralama():
    letter=input("Lutfen arasina tire(-) ekleyerek birden fazla kelime yaziniz:")
    dizi=letter.split("-")      #split ile - lerden ayirdik
    dizi.sort()                 # sort ile siraladik
    return print(*dizi, sep="-")
siralama()