def fonk(a):        #fonksiyon belirtilen sayıya kadar o sayının bölenlerini hesaplar ardından bölenler toplamının sayıya eşitliğini ineler
    bölenler=[]
    for i in range(1,a):
        kalan=a%i
        if kalan==0:
            bölenler=bölenler+[i]
    topla=0
    for i in bölenler:
        topla+=i
    if topla==a:
        return print(a)
while True:
    try:
        for i in range(1000):
            fonk(i)
        seçim=input("\n*****Devam etmek için her hangi bir tuşa  ///  çıkmak için (q) tuşuna basınız..:")
        if seçim=="q" or seçim =="Q":
            break
    except ValueError:
        print("Lütfen bir tam sayı giriniz..:")
        continue



