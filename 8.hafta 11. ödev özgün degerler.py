def tekrarsil(a):
    küme=set(a)
    liste=list(küme)
    print(liste)
    

print("lütfen girmek istediğiniz degerleri sıra ile yazınız... BİTİNCE 'Q' / 'q' TUŞUNA BASINIZ...")
degerliste=[]

while True:
    a=input("\n")
    if a=="q" or a=="Q":
        break
    else:
        degerliste+=[a]
        
print(degerliste)
tekrarsil(degerliste)
