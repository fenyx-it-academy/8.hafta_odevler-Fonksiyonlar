a="cdd-z-e-t-aaa-bbb-ddd"

harf=["A","B","C","D","E","F","G","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","W","Q","Z","a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","w","q"]
sayıliste=[]
sayılistetam=[]
mliste=a.split("-")
print(mliste)
yeniliste=mliste.copy()
##enuzunkelime=0
#ksıra=0
ksayı=len(mliste)       #kelime sayısı
khsıra=0        #kelime içi harf sıra
hno=0        #harfin alfabedeki sıralaması
hnod=0      #diğer kelimenin harf nosu
i=-1
for r in range(len(mliste)):
    for i in mliste[r]:
        print(mliste[r])
        sayıliste+=[i]
    sayılistetam[r]=[sayıliste]
print(sayılistetam)
        
    
