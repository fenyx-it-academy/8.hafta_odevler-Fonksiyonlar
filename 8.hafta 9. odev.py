print('b.')
'''
9-Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf sayılarının veren bir fonksiyon yazınız
'''
def buyuk_kucuk_harf():
     buyuk_harf=0                   # buyuk ve kucuk harf sayilarini baslangicta sifir olarak aldik
     kucuk_harf=0
     for i in letter:               # for ile girilen ifadenin harflerini inceledik
         if i.isupper()==True:      # buyuk harf kontrolu
             buyuk_harf +=1         # degerleri 1 arttirdik
         elif i.islower()== True:      # kucuk harf kontrolu
             kucuk_harf +=1            # degerleri 1 arttirdik
     return f' buyuk harf sayisi : {buyuk_harf} \n kucuk harf sayisi : {kucuk_harf}'
letter=input("icersindeki buyuk ve kucuk harf sayilarini bulmak istediginiz ifadeyi giriniz :")
print(buyuk_kucuk_harf())