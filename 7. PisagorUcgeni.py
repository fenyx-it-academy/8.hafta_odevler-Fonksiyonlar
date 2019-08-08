# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları
# ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

print(''''
      
      |\ 
      | \ c                        
    b |  \      pisagor ucgeni => c^2 = a^2 + b^2 (uzun kenarin karesi kisa kenarlarin karesinin 
      |___\                                        toplamina esit ise o ucgen pisagor ucgenidir)
        a                                               
         
''')

def pisagor():
    anaListe = []
    pisagorUcgenler = []
    for c in range(1, 101):
        for b in range(1, 101):
            for a in range(1, 101):
                if c > b and c > a:
                    #buyuk kenari c olarak belirledigimiz icin
                    #b ve a nin cden buyuk oldugu secenekleri islem disinda birakiyoruz

                    if pow(c, 2) == (pow(b, 2) + pow(a, 2)):
                       #cnin karesi b ce anin kareleri toplamina esit ise;
                       if c and b and a not in pisagorUcgenler:
                            #c,b,a pisagorUcgenler listemiz icinde var ise tekrar islem yapma
                            pisagorUcgenler = []
                            #bir onceki uclunun uzerine ekleme yapmasin diye listeyi sifirladik

                            pisagorUcgenler.append(c)
                            pisagorUcgenler.append(b)
                            pisagorUcgenler.append(a)

                            #ucgen degerlerini siraladik
                            pisagorUcgenler.sort()

                            #pisagor ucgeni olusturan degerleri sirayla ana listeye ekledik
                            anaListe.append([i for i in pisagorUcgenler])

    return print('1den 100e kadar olan sayılardan pisagor üçgeni oluşturanlar:\n',anaListe)

try:
    pisagor()
except:
    print('Hatali islem. Program sonlandirildi.. ')
