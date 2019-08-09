# coding=utf-8
def harf_sayısı(veri):
    #foksiyon ve parametre tanımlama
    buyuk_harf=0
    kucuk_harf=0
    #buyuk-kucuk harf sayısını tutacak degisken
    metin=list(str(veri))
    #girilen verinin listeye donusturulmesi
    for i in metin:
        #liste icinde dongu
        kontrol=''
        #hafrin buyutulmus halinin tutulacagı degisken
        if i.isalpha()==True:
        #dongudeki i nin harf olup-olmadıgının kontrolu
            kontrol=i.upper()
            #harfi buyuk harf yapıp degiskene atama
            if i==kontrol:
                #kontrole atanan harf eski haliyle aynıysa harf zaten buyuktur
                buyuk_harf+=1
                #buyuk harf degiskenini bir artır
            else:
                #kontrole atana harf eski hliyle aynı degilse
                kucuk_harf+=1
                #kucuk harf degiskenini bir artır
    return print(f'Girilen verideki büyük harf sayısı {buyuk_harf}, küçük harf sayısı {kucuk_harf} tanedir.')






