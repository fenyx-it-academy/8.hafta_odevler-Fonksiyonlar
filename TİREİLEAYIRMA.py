"""Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan
ve sonrasında bu kelimeleri harf sırasına göre dizip tekrar
tire ile ayırıp output olarak veren bir fonksiyon yazınız.
örnek girdi: green-red-yellow-black-white örnek çıktı:
 black-green-red-white-yellow"""

def ters():
    girdi=input("'-' ile ayrılan bir liste olusturunuz: ")
    girdi=girdi.split("-")
    girdi.sort()
    print( *girdi,sep="-")
ters()
