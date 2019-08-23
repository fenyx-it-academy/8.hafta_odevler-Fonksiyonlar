'''
8-Pozitif bir tamsayının faktöriyelini alan bir fonksiyon yazınız.
'''

def faktöriyel(sayı):

    for i in range(1,sayı):
        sayı*=i

    return print(sayı)

faktöriyel(6)
