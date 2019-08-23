
'''
10-Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve
sonrasında bu kelimeleri harf sırasına göre dizip tekrar tire ile ayırıp
output olarak veren bir fonksiyon yazınız. örnek girdi: green-red-yellow-black-white
örnek çıktı: black-green-red-white-yellow
'''

def sıralama():
    harf = input("Lütfen aralarına tire(-) ekleyerek birden fazla kelime yazınız: ")
    dizi = harf.split("-")  # split ile - lerden ayırdık
    dizi.sort()             # sort ile sıraladık
    return print(*dizi, sep="-")
sıralama()
