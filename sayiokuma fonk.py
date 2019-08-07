#Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
# Örnek: 97 ---------> Doksan Yedi

def sayi_oku(rakam=(input('1.yol en cok 3 basamakli sayiyi giriniz :'))):
    if rakam.isdigit()==False:
        print('lutfen 3 basamakli sayi giriniz')
        return

    birler =['','bir','iki','üç','dört','beş','altı','yedi','sekiz','dokuz']
    onlar  =['','on','yirmi','otuz','kırk','elli','altmış','yetmiş','seksen','doksan']
    yuzler =['yüz']
    goster =[]
    #rakam bir basamakliysa girilen sayi birler listesindeki indexe giderek kendi sayisini okuyor
    #ornek olarak rakam[0] =5 ise bu deger birler[5] deki degere 'bes' e gitmis oluyor
    if len ( rakam ) == 1:
        goster = [birler[int ( rakam[0] )]]
        print (rakam,'------>' ,*goster )
    #rakam iki basamakli ise rakam[0]=onlar listesi ve rakam[1]= birler listesindeki indexlere
    #giderek kendi degerlerini bulmus olurlar
    ##ornek olarak rakam[0] =3 --->onlar[3]'otuz' ve rakam[1] =5 ---> birler[5] 'bes'
    elif  len(rakam)==2:
        goster = [onlar[int ( rakam[0] )] , birler[int ( rakam[1] )]]
        print (rakam,'------>' ,*goster)
    # rakam uc basamakli ise rakam[0]=yuzler listesi,rakam[1]=onlar listesi ve rakam[2]= birler listesindeki indexlere
    # giderek kendi degerlerini bulmus olurlar

    elif len(rakam)==3:
        if int(rakam[0])==1: #sadece yuz yazdirmak  icin bu dongu kuruldu

            goster = [yuzler[0] , onlar[int ( rakam[1] )] , birler[int ( rakam[2] )]]
            print(rakam,'------>' ,*goster)

        elif int(rakam[0])==0: #yuzler basamagi 0 ise onlar ve birler basamagi yazilacak
            goster = [onlar[int ( rakam[1] )] , birler[int ( rakam[2] )]]
            print ( rakam,'------>' ,*goster)

        else :
            goster =[birler[int(rakam[0])]+yuzler[0],onlar[int(rakam[1])],birler[int(rakam[2])]]
            print (rakam,'------>' ,*goster)

    else:
        print('lutfen 3 basamakli sayi giriniz')
#--------------------------------------------
sayi_oku()

#--------------------------------------------
#sayinin 4 basamakli olmasi saglandi zfill(4) fonksiyonuyla
def sayi_oku2(rakam=input('2.yol en cok 4 basamakli sayiyi giriniz ').zfill(4)):
    if len(rakam)>4:
        print('lutfen 4 basamakli sayi giriniz')
        return
    elif rakam.isdigit()==False:
        print('lutfen 4 basamakli sayi giriniz')
        return

    birler =['','bir','iki','üç','dört','beş','altı','yedi','sekiz','dokuz','']
    onlar  =['','on','yirmi','otuz','kırk','elli','altmış','yetmiş','seksen','doksan']
    yuzler =['','yüz','ikiyüz','üçyüz','dörtyüz','beşyüz','altıyüz','yediyüz','sekizyüz','dokuzyüz']
    binler =['','bin','ikibin','üçbin','dörtbin','beşbin','altıbin','yedibin','sekizbin','dokuzbin']
    #hep 4 basamakli oldugu icin rakam[0]=binler ,rakam[1]=yuzler,rakam[2]=onlar,rakam[3]=birler listesindeki
    #indexler ile esli
    #3045 binler[3],yuzler[0],onlar[4],birler[5]

    goster =[binler[int ( rakam[0] )],yuzler[int ( rakam[1] )], onlar[int ( rakam[2] )] , birler[int ( rakam[3] )]]
    print (rakam,'------>:',*goster )
#----------------------------------------------------

sayi_oku2()
