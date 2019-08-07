""" Asal sayi olup olmadigini kontrol eden fonksiyon yazınız."""

def asal_sayi(number):
    sayac=0
    for i in range(2,number):
        if number%i==0 :
             sayac+=1
    if sayac!=0:
        return "sayi asal degildir"
    return "sayi asaldir"

print(asal_sayi(24))


