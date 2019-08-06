##Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon
##yazınız. örnek: madam, taco cat, utrecht sonuç: True, True, False
while True:
    def ters(a):
        liste=[]
        for i in a:
            liste+=[i]
        tersliste=liste[::-1]
        terskelime="".join(tersliste)
        if a==terskelime:
            return 'True'
        else:
            return 'False'

    veri=input("Lutfen bir metin giriniz cikis icin 'q':").lower()
    if veri=='q':
        break
    sonhal="".join(veri.split())
      
    print(ters(sonhal),"\n")

