##Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve sonrasında bu
##kelimeleri harf sırasına göre dizip tekrar tire ile ayırıp output olarak
##veren bir fonksiyon yazınız. örnek girdi: green-red-yellow-black-white
##örnek çıktı: black-green-red-white-yellow

def sirala(a):
    liste=a.split("-")
    liste.sort()
    "-".join(liste)
    return liste
verilenliste=input("Lutfen '-' ile ayrilan listenizi olusturunuz:")
print(sirala(verilenliste))
