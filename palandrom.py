# coding=utf-8
def palindrom(veri):
    #fonksiyon ve parametre tanımlama
    liste=list(veri)
    #girilen veriyi listeye donusturme
    liste.reverse()
    #listenin ogelerinin sırasını tersine çevirme
    if liste==list(veri):
        #tersten liste ile verinin listeye donuturlmusu esit olma durumu
        return print(f'{veri} palindromdur.')
        #return ile soncu ekrana yazdırma
    else:
        #listelerin esit olmama durumu
        return print(f'{veri} palindrom değildir.')
        #return ile ekran cıktuus

