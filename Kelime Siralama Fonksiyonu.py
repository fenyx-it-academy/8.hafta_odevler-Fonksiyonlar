"""
10. Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve
sonrasında bu kelimeleri harf sırasına göre dizip tekrar tire ile ayırıp output olarak veren bir fonksiyon yazınız.
örnek girdi: green-red-yellow-black-white örnek çıktı: black-green-red-white-yellow
"""

def kelime_siralama():
    kelime_sirasi= input("Lutfen (-)Tire ile ayirarak birden fazla kelime giriniz:")
    kelimeler=kelime_sirasi.split("-")
    kelimeler.sort()
    print(*kelimeler,sep="-")

kelime_siralama()