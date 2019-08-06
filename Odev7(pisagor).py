##1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran
##bir fonksiyon yazın.(a <= 100,b <= 100)   
def pisagor():
    liste=[]
    for i in range(1,150):
        liste+=[float(i)]
    listecift=[]
    for x in range(1,101):
        for y in range(1,101):
            listecift+=[[x,y]]
    sayac=0
    sonliste=[]
    while sayac<len(listecift):
        a=(listecift[sayac])
        c=((a[0]**2)+(a[1]**2))**0.5
        sayac+=1
        if c in liste:
            sonliste+=[a]    
        else:
            continue
    return sonliste
print(pisagor())
