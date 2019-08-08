# Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan ve sonrasında bu kelimeleri
# harf sırasına göre dizip tekrar tire ile ayırıp output olarak veren bir fonksiyon yazınız.
# örnek girdi: green-red-yellow-black-white örnek çıktı: black-green-red-white-yellow

try:
    def alfabetikSirala(str):
        str = str.split('-')
        str.sort()
        str = '-'.join(str)

        print(str)

    alfabetikSirala('green-red-yellow-black-white')
except:
    print('Hatali islem. Program sonlandirildi..')
