#Bu kod iki basamakli sayilarin okunusunu gosterir


def onluk(say):
    onlukoku={
    '1':"on",
    '2':"yirmi",
    '3':"otuz",
    '4':"kirk",
    '5':'elli',
    '6':'altmis',
    '7':"yetmis",
    '8':'seksen',
    '9':'doksan'
    }
    onlarbasamagi=say[0]
    return onlukoku[onlarbasamagi]

def birlik(say):
    birlerbasamagi =say[1]
    if birlerbasamagi=='1':
        return 'bir'
    elif birlerbasamagi=="2":
        return'iki'
    elif birlerbasamagi=='3':
        return 'uc'
    elif birlerbasamagi=='4':
        return 'dort'
    elif birlerbasamagi=='5':
        return 'bes'
    elif birlerbasamagi=='6':
        return 'alti'
    elif birlerbasamagi=='7':
        return "yedi"
    elif birlerbasamagi=='8':
        return "sekiz"
    elif birlerbasamagi=='9':
        return 'dokuz'
    elif birlerbasamagi=='0':
        return ""

while True:
    sayi=input("Yazdirmak istediginiz sayiyi giriniz(cikis icin q):")
    if sayi=="q":
        break
    elif sayi.isdigit() and len(sayi)==2:
        print('{} nin okunusu: {}{} dir'.format(sayi,onluk(sayi),birlik(sayi)))

    else:
        print('iki basamakli bir sayi giriniz')

