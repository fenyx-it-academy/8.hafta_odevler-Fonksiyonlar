# coding=utf-8
def perfect_number(sayı):
    # fonksiyon tanımlama
    try:
        if sayı>=1000:
            # 1000den buyuk sayılar icin uyarı
            return print('Lütfen 1000 den küçük bir tamsayı giriniz.')

        bolen_list=[]
        #bolenlerin biriktirilecegi liste
        for i in range(1,sayı):
            #1 den sayıya kadar dongü
            if sayı%i==0:
                #girilen sayı dongudeki sayılara bolunüyorsa listeye ekle
                bolen_list+=[i]

        if sayı==sum(bolen_list):
            #sayı listedeki sayıların toplamına esitse
            #mükemmel sayısını return ile ekrana yazdır
            return print(f'{sayı} sayısı mükemmel sayıdır.')

        else:
            #yukarıdaki sartlar saglanmıyorsa
            #sayı mukemmel sayı degildir yazısını return ile ekrana yazdır
            return print(f'{sayı} sayısı mükemmel sayı değildir.')

    except:
        #hatalı giris uyarısı
        return print('Girdiğiniz sayının tamasayı olduğundan emin olunuz.')


