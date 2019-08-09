

def terskontrol(a):
    metin=list(a)
    tyazı=""
    for i in metin:
        tyazı=i+tyazı
    print("\n",a,"-------------->",tyazı)
    if a==tyazı:
        print("\nTrue")
    else:
        print("\nFalse")
        
while True:
    metin=input("\nTersi ile aynı olup olmadığını kontrol etmek istediğiniz sözcüğü yazınız..\n")
    terskontrol(metin)
    devam=input("\nDevam etmek için herhangi bir tuşa çıkmak için 'q' / 'Q' tuşuna basınız..")
    if devam== 'Q' or devam =='q':
        break
    
