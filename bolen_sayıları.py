def tam_bol(sayı): #fonksiyon ismi tanımlama
    try:
        tambolen_listesi=[] #tam bolenlerin biriktirilecegi liste
        for i in range(1,sayı+1): #1 den girilen sayıya kadar dongü
            if sayı%i==0: #verilen sayının dongüdeki herbir sayıya bolunup-bolunmediginin kontrolu
                tambolen_listesi+=[i] #bolen sayıların listeye eklenmesi
        return print(*tambolen_listesi) #bolen listesini return ile ekrana yazdırma
    except:
        print('Lütfen girdiğiniz sayıyı kontrol ediniz.') #hatalı giris uyarısı

tam_bol(60)
