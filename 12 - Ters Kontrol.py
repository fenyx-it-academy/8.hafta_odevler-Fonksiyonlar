def tersi(*args):
    kelime_ters=""
    sonuc=[]
    for i in args:
        for j in range(len(i)-1,-1,-1):
            kelime_ters+=i[j]
        print(kelime_ters)
        if i==kelime_ters:
            sonuc.append(True)
            kelime_ters = ""

        else:
            sonuc.append(False)
            kelime_ters = ""

    return sonuc


