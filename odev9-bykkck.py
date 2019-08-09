def bykkck():
    byk='QWERTYUIOPLKJHGFDSAZXCVBNM'
    kck='qwertyuioplkjhgfdsazxcvbnm'
    harfler=input('Lutfen bir kelime giriniz')
    sayacbyk=0
    sayackck=0
    for i in harfler:
        if i in byk:
            sayacbyk+=1
        if i in kck :
            sayackck+=1
    print(f'Buyuk harf sayisi{sayacbyk}\nKucuk harf sayisi{sayackck}')
#daha once belirledigimiz buyuk ve kucuk harfleri
#for dongusu ile buyuk ve kucuk olanlari saydik ve kullaniciya print olarak verdik
bykkck()