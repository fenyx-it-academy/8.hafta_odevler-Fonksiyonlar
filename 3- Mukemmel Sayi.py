def mukemmelsayislemi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:       # Girilen sayiya kadar olan rakamlar ile girilen sayiyi boluyor
            toplam += i         # kalani o olanlari toplayarak gidiyor
    if sayi == toplam:
        return True         # Toplayarak gittigi sayilar o andaki bolene esit ise islemi yap diyor olumlu diyir


m_s_listesi = []

for i in range(1, 1000):
    if mukemmelsayislemi(i):
        m_s_listesi.append(i)  # listeye ekledik.

print("Mükemmel sayılar : ", m_s_listesi)