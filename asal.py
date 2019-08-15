#odev 1#
#asal sayı kontrol#

print("bir sayi giriniz ve asal olup olmadigini kontrol ediniz")
def asal(a):
    
    if a<=0 or a==1 or a==2:
        return "Asal sayı degildir,2 den buyuk bir sayi giriniz"
    else:
        for i in range(2,a):
            if a%i==0:
                return "girmis oldugunuz sayı asal degildir"
    return "bu sayı asal bir sayıdır"
print(asal(int(input("bir sayı giriniz:"))))
                    
            
