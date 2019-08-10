#  Kullanıcıdan tire(-) ile ayrılan bir input dizisi
#  alan ve sonrasında bu kelimeleri harf sırasına
#  göre dizip tekrar tire ile ayırıp output olarak veren bir fonksiyon yazınız.
# örnek girdi: green-red-yellow-black-white
# örnek çıktı: black-green-red-white-yellow

def reorder(words):
    items = words.split("-")
    items.sort()
    return ("-".join(items))
while True:
    words = input("Please enter your words followed by dash!\n")
    if words== "q" or words=="Q":
        print("exits!")
        break
    print(reorder(words))

