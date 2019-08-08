
def pisagor():
    kume=[]

    for a in range(1,100):
        for b in range(1,100):
            c = a**2 + b**2
            c=c**0.5
            for d in range(100):
                if c==d and c<100:
                    kume +=[sorted([a,b,int(c)])]

    print(kume)

pisagor()
