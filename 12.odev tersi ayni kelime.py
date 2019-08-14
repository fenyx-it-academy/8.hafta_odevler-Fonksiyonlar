##12. Verilen inputların tersten de aynı olup
##olmadığını kontrol eden bir fonksiyon yazınız.
##örnek: madam tacocat utrecht
##sonuç: True, True, False


kul=input("rasgele kelimeler yaziniz : ")
AyrilmisListe=kul.split()
aa=AyrilmisListe
print(aa)
sayac=0
ekle=[]
while sayac<=len(aa)-1:
    if aa[sayac] == aa[sayac][::-1]:
        ekle += ['True']
        
    if aa[sayac] != aa[sayac][::-1]:
        ekle += ['False']
    sayac+=1
print(*ekle,sep=",")
    
        
    
