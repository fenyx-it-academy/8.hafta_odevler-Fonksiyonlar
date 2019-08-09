def okuma(sayı):
        bb=sayı%10
        oo=sayı// 10
        ooy=""
        bby=""
        if oo==1:
            ooy="on"
        elif oo==2:
            ooy="yirmi"
        elif oo==3:
            ooy="otuz"
        elif oo==4:
            ooy="kırk"
        elif oo==5:
            ooy="elli"
        elif oo==6:
            ooy="altmış"
        elif oo==7:
            ooy="yetmiş"
        elif oo==8:
            ooy="seksen"
        elif oo==9:
            ooy="doksan"
        if bb==1:
            bby="bir"
        elif bb==2:
            bby="iki"
        elif bb==3:
            bby="üç"
        elif bb==4:
            bby="dört"
        elif bb==5:
            bby="beş"
        elif bb==6:
            bby="altı"
        elif bb==7:
            bby="yedi"
        elif bb==8:
            bby="sekiz"
        elif bb==9:
            bby="dokuz"
        elif bb==0:
            bby=" "
        print("\n",ooy,bby,sep="")

while True:
    try:
        sayım=int(input("\nLütfen Sayıyı rakamlarla yazınız"))
        okuma(sayım)
        seçim=input("\n***  Çıkmak için 'q' / 'Q' tuşuna, devam etmek için herhangi bir tuşa basınız  *** :")
        if seçim=="q" or seçim =="Q":
            break
    except ValueError:
        print("\n!!!!  Lütfen Rakamlardan oluşan bir sayı giriniz..:")
