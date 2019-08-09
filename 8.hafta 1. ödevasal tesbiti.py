
def fonk(a):
    bölenler=[]
    for i in range(1,a+1):
        kalan=a%i
        if kalan==0:
            bölenler=bölenler+[i]
            g_bölen=bölenler[:]
    g_bölen.remove(1)
    g_bölen.remove(a)

    if len(g_bölen)==0:    
        return "Bu sayı asaldır"
    else:
        return "Bu sayı asal değildir"

while True:
    try:
        sayı= int(input("Asal olup olmadığını merak ettiğiniz sayıyı giriniz..:"))
        print(fonk(sayı))
        seçim=input("\nDevam etmek için her hangi bir tuşa, çıkmak için q tuşuna basınız..:")
        if seçim=="q" or seçim =="Q":
            break
    except ValueError:
        print("Lütfen bir tam sayı giriniz..:")
        continue



