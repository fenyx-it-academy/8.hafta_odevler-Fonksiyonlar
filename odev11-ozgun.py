def ozgun(*args):
    metin=[]
    for i in args:
        metin.append(i)

    metin=set(metin)
    metin=list(metin)
    print(*metin)
ozgun(1,2,5,4,4,4,8,5,9,5,'AA','aa','aa')