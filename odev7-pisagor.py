def pisagor():
    for z in range(1,100):
        for x in range(1,100):
            for y in range(1,100):
                if (x**2+y**2)==z**2 :
                    print(x,y,z)
#for dongusu ile ucgenin uckenarinin herbirini
#1 den 100 e kadar siraladik ve if ile pisagor
#olma durumunda bunu printlemesini sagladik
pisagor()