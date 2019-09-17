def faktoriyel(sayı):
    faktor =1
    for i in range(1,sayı+1):
        faktor *=i
    return faktor

numara = int(input("bir sayı giriniz:"))
a = faktoriyel(numara)
print(a)
    
