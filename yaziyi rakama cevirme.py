#Kullanici inputu ile ggggyaziyla verilen sayinin sayisal degerini bulunuz
#ornek elli yedi----->57


def okunan_yazi(sayioku=input('Bulmak istediginiz sayiyi yaziyla bırer boşluk birakarak yaziniz ''\n'
                              'örnek(dokuzyüz doksan dokuz)   :').lower()):



    birler  = ['','bir','iki','üç','dört','beş','altı','yedi','sekiz','dokuz'                         ]
    onlar   = ['','on','yirmi','otuz','kırk','elli','altmış','yetmiş','seksen','doksan'               ]
    yuzler  = ['','yüz','ikiyüz','üçyüz','dörtyüz','beşyüz','altıyüz','yediyüz','sekizyüz','dokuzyüz' ]


    #birler onlar yuzler listesinin disinda karakter girilmismi onu kontrol ediyor
    hata=[True for bak in sayioku.split() if bak not in birler if bak not in onlar if bak not in yuzler]

    if hata==[True]:
        print('yazim hatasi algilandi')
        return


    # birler onlar yuzler basamaklari icin split() ile listeye ceviriliyor her yazili sayi
    #tek tek bir_oku,onlar_oku,yuzler_oku icerisinde okunuyor ve burasi onemli
    #INDEX i aliniyor bulunan index degeri  (bir_oku x 1,onlar_oku x 10,yuzler_oku x 100)ile carpilir

    bir_oku    = [birler.index ( ayir ) for ayir in sayioku.split () if ayir in birler]
    onlar_oku  = [onlar.index  ( ayir ) for ayir in sayioku.split () if ayir in onlar ]
    yuzler_oku = [yuzler.index ( ayir ) for ayir in sayioku.split () if ayir in yuzler]

    print (sayioku,'---->', sum ( bir_oku + 10 * onlar_oku + 100 * yuzler_oku ) )#sum() komutu ile toplamlari alinir
    #ornegin bir_oku=3,onlar_oku=5x10,yuzler_oku=9x100 toplamlari=900+50+3=953



okunan_yazi()
