#Kullanıcıdan tire(-) ile ayrılan bir input dizisi alan
# ve sonrasında bu kelimeleri harf sırasına göre dizip tekrar tire ile
# ayırıp output olarak veren bir fonksiyon yazınız.
# örnek girdi: green-red-yellow-black-white örnek çıktı:
# black-green-red-white-yellow



def siralama(kelime=input ( "Lutfen Kelimeleri '-' ile Ayirin :" ).upper() ):
    goster = []
    sirala=''
    for sayac in kelime.split('-') :#kelimeleri - isaretinin oldugu yerden ayirarak liste olustu
        goster += [sayac]
    goster.sort()                   #liste harf sirasina gore siralandi

    for ekle in goster[0:len(goster)]:
        sirala+=(ekle+'-')          #siralanan liste kelimelere '-'eklendi

    return sirala[:-1]              #burada son kelimeyede '-'  eklendigi icin son karakteri gostermiyoruz


print(siralama())
