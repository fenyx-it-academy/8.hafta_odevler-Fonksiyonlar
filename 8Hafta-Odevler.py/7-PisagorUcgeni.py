"""Pisagor olusturma"""
def pisagor():
    pisagor_liste = list()#bos liste
    for a in range(1,101):#i ve j sayisinin dongusu
        for b in range(1,101):
            c = (i ** 2 + j ** 2) ** 0.5#c sayisinin degeri
            if c == int(c):#c int ise listeye a,b,c dgerlerini yaz
                pisagor_liste.append((a,b,int(c)))

    return pisagor_liste#listeyi dondur
print(pisagor())
