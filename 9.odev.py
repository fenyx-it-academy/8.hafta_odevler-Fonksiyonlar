'''
9-Kullanıcıdan bir input alan
 ve bu inputun içindeki büyük ve küçük harf sayılarının veren bir fonksiyon yazınız.
'''

def büyük_küçük_harf():
     büyük_harf=0                   # büyük ve küçük harf sayılarını başlangıçta sıfır olarak aldık
     küçük_harf=0
     for i in harf:               # for ile girilen ifadenin harflerini inceledik
         if i.isupper()==True:      # büyük harf kontrolü
             büyük_harf +=1         # değerleri 1 arttırdık
         elif i.islower()== True:      # küçük harf kontrolü
             küçük_harf +=1            # değerleri 1 arttırdık
     return f' büyük harf sayısı : {büyük_harf} \n küçük harf sayısı : {küçük_harf}'
harf=input("içersindeki büyük ve küçük harf sayılarını bulmak istediğiniz ifadeyi giriniz :")
print(büyük_küçük_harf())
