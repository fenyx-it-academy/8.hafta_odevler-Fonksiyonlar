#odev 7#
#pisagor olusturma#

def pisagor():
    liste=[]
    for a in range(1,101):
        for b in range(1,101):
            c = (a** 2 + b ** 2) ** 0.5
            if c == int(c):
                liste.append((a,b,int(c)))

    return liste
print(pisagor())
