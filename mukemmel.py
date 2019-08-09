#odev3#
#mukemmel sayı#

print("""mukemmel sayı bölenleri toplami kendisine esit olay sayıdır.
1-1000 arasi mukemmel sayilar asagida listelenmistir.\n""")
def mukemmel(a):
    toplam=0
    for i in range(1,a):
        if a%i==0:
            toplam+=i
    if toplam == a:
            return True

for i in range(1,1000):
    if mukemmel(i)==True:
        print(i)
    
