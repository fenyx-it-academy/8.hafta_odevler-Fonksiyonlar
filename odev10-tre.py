def tre():
    metin=input('Lutfen kelimeleri girin ve arasina tire isareti koyun!:')
    # metin=list(metin)
    if '-' in metin:
        metin=metin.split('-')
        metin.sort()
        print(*metin,sep='-')
    else:
        print('Metininde "-" karrakteri bulunamadi!')
tre()