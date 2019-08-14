##7.odev: 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları
##ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

for c in range(100):
    for b in range(c):
        for a in range(b):
            if c**2==a**2+b**2: #ic ice dongu kurarak formulu isletiyoruz
                print(f'a={a} : b={b} : c={c}')

