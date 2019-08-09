def fonk(a):        #fonksiyon belirtilen sayıya kadar o sayının bölenlerini hesaplar ardından bölenler toplamının sayıya eşitliğini ineler
    bölenler=[]
    for i in range(1,a):
        kalan=a%i
        if kalan==0:
            bölenler=bölenler+[i]
    return bölenler
while True:
    try:
        sayı1=int(input("1. sayıyı giriniz ...:"))
        sayı2=int(input("2. sayıyı giriniz ...:"))
        bölenler1=fonk(sayı1)
        bölenler2=fonk(sayı2)
        böl1=set(bölenler1)
        böl2=set(bölenler2)
        print("\nBu iki sayının pozitif bölenleri sırası ile aşağıda verilmiştir.\n",bölenler1,"\n",bölenler2)
        ortak=böl1.intersection(böl2)
        ortak=list(ortak)
        ebob=max(ortak)
        yazı="{} ile {} sayısının ebobu ,"
        print("\n",yazı.format(sayı1,sayı2),ebob, "dur")
    except ValueError:
        print("lütfen tam sayı giriniz..")
        continue
    
    seçim=input("\n*****Devam etmek için her hangi bir tuşa  ///  çıkmak için (q) tuşuna basınız..:")   
    if seçim=="q" or seçim =="Q":
        break
    




