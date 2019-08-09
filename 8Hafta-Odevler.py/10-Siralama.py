"""Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve sonrasında bu kelimeleri harf sırasına göre dizip tekrar tire ile ayırıp output olarak veren bir fonksiyon yazınız.
örnek girdi: green-red-yellow-black-white
örnek çıktı: black-green-red-white-yellow"""
def sirala(s):#split ile altigimiz stringi listelarak boluyoruz
              #sorted ile harf sirasina gore dizip join ile tekrar stringe donusturuyoruz
    return ("-".join(sorted(s.split("-"))))
while True:
    try:#strin disinda bir degerde hatayi yakala
        s = input("arasina tire(-) koyarak birkac sozcuk yazin: ")
        print(sirala(s))
    except:
        print("bir hata olustu")