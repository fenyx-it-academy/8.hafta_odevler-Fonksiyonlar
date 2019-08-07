"""7. 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)"""

from math import sqrt

def pisagor():
    ucgenler=[]
    ucgen=[]

    for i in range(1,101):
        for j in range(1,101):
            c=i**2 + j**2
            ucuncu_kenar = sqrt(c )
            if  int(ucuncu_kenar)== ucuncu_kenar and ucuncu_kenar<100 :
                ucgen.append(i)
                ucgen.append(j)
                ucgen.append(ucuncu_kenar)
        ucgenler.append(ucgen)

    return ucgenler
print(pisagor())