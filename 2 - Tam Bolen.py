

def TambolumIslemi(a):
    Toplam_TamBolen = []
    for i in range(1, a + 1):
        if a % i == 0:
            Toplam_TamBolen.append(i)
    return Toplam_TamBolen

while True:
    a = int(input("Sayıyi Giriniz : "))
    print(a, "Sayisinin Tam Bolenleri :", TambolumIslemi(a),"\n")