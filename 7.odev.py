'''
7- 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları
 ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
'''

def pisagor_üçgeni():

    liste = []

    for a in range(1,101):
        for b in range(1,101):
            d = a**2 + b**2 #c kareye eşitlediğimde hata aldığımdan dolayı d değeri ne eşitledim
            c = d**0.5 # c yide d nin kareköküne eşitleyerek sorunun üstesinden geldim
            if c == int(c):
                liste.append([a, b, int(c)])

    return print(liste)

pisagor_üçgeni()
