##Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK)
##dönen bir tane fonksiyon yazın.
while True:
    def ekok(sayi1,sayi2):
        liste1=[]
        liste2=[]
        yeni_sayi1=0
        yeni_sayi2=0
        while len((set(liste1)).intersection(set(liste2)))<1:
            yeni_sayi1+=sayi1
            yeni_sayi2+=sayi2
            liste1+=[yeni_sayi1]
            liste2+=[yeni_sayi2]
        return (set(liste1)).intersection(set(liste2))
    ilksayi=input("Lutfen birinci sayiyi giriniz cikis icin 'q':").lower()
    if ilksayi=='q':
        break
    ikincisayi=int(input("Lutfen ikinci sayiyi giriniz:"))
    print(ilksayi," ve ",ikincisayi,",sayilarinin EKOK'u: ",list(ekok(int(ilksayi),ikincisayi))[0],"\n",sep="")

        
  
    
                                                    
