def fonk(a,b):        #fonksiyon iki sayının ortak katlarından en küçüğünü alır..
    akatlar=set()       #a ve b nin katları ile birer küme oluşturulur
    bkatlar=set()
    k=0
    while True:
        k+=1
        ka=k*a
        kb=k*b
        akatlar.add(ka)         #a nin katlarının oluşturduğu kümeye sırayla a nin 1.2.3. katları eklenir.
        bkatlar.add(kb)         #b nin katlarının oluşturduğu kümeye sırayla b nin 1.2.3. katları eklenir.
        if len(akatlar.intersection(bkatlar))==1:    #ave b sayılarının katlarının oluşturduğu kümelerin kesişim kümsinin eleman sayısı
            ekoklist=list(akatlar.intersection(bkatlar))
            ekok=ekoklist[0]
            yazı="\n{} ile {} sayısının ekoku  "
            print(yazı.format(sayı1,sayı2),ekok)
            break
while True:
    try:
        sayı1=int(input("1. sayıyı giriniz ...:"))
        sayı2=int(input("2. sayıyı giriniz ...:"))
        fonk(sayı1,sayı2)
        
    except ValueError:
        print("lütfen tam sayı giriniz..")
        continue
    
    seçim=input("\n*****Devam etmek için her hangi bir tuşa  ///  çıkmak için (q) tuşuna basınız..:")   
    if seçim=="q" or seçim =="Q":
        break
    




