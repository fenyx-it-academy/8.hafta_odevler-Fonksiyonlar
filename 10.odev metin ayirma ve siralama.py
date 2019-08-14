##10. Kullanıcıdan tire(-) ile ayrılan bir input dizisi
##alan ve sonrasında bu kelimeleri harf sırasına göre
##dizip tekrar tire ile ayırıp output olarak veren bir
##fonksiyon yazınız.
##örnek girdi: green-red-yellow-black-white
##örnek çıktı: black-green-red-white-yellow

def siralama(kul=input("En son gezdiginiz 5 sehrin isimlerini aralarina - koyarak yaziniz : ")):
    ayir=kul.split("-")          ##metin liste haline getirildi 
    ayir.sort()                  ##liste harf sirasina gore siralandi
    liste=''
    for ekle in ayir[0:len(ayir)]:
        liste+=(ekle+'-')
    return liste[:-1]             ##liste sonundaki '-' kaldirildi      
print(siralama())


        
