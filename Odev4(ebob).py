##Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB)
#dönen bir tane fonksiyon yazın.

while True:
    def ebob(sayi1,sayi2):
        liste1=[]
        liste2=[]
        for i in range(1,sayi1+1):
            if sayi1%i==0:
                liste1+=[i]
        for x in range (1, sayi2+1):
            if sayi2%x==0:
                liste2+=[x]
        kume1=set(liste1)
        kume2=set(liste2)
        return max(kume1.intersection(kume2))
    ilksayi=input("Lutfen birinci sayiyi giriniz cikis icin 'q':").lower()
    if ilksayi=='q':
        break
    ikincisayi=int(input("Lutfen ikinci sayiyi giriniz:")) 
    print(ilksayi," ve ",ikincisayi,", sayilarinin EBOB'u: ",ebob(int(ilksayi),ikincisayi),"\n",sep="")
    
