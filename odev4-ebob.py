def ebob(sayi1,sayi2):
    ilksayi=[]
    ikincisayi=[]
    ebob=[]
#sayilarimizi kaydedecegimiz bos listeler actik
#for donguleri ile sayilari tam bolen sayilari bulduk
#ve bunlari actigimiz listelere kaydettik
    for i in range(2,sayi1+1):
        if sayi1%i==0:
            ilksayi.append(i)
    for i in range(2,sayi2+1):
        if sayi2%i==0:
            ikincisayi.append(i)
#iki listedeki sayilari karsilastirarak ayni olan sayilari bulduk
    for i in ilksayi:
        for x in ikincisayi :
            if i==x :
                ebob.append(i)
#buldugumuz sayilari listelere kaydettikten sonra max kullanarak
#bunlarin icinde en buyugunu print olarak ekrana verddik

    print(max(ebob))
ebob(12,48)
