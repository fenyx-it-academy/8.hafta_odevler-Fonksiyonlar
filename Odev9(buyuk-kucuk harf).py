##Kullanıcıdan bir input alan ve bu inputun içindeki büyük ve küçük harf
##sayılarının veren bir fonksiyon yazınız.
kucuk_harfler="abcçdefgğhıijklmnoöqprsştuüwxvyz"
buyuk_harfler="ABCÇDEFGĞHIİJKLMNOÖQPRSŞTUÜWXVYZ"
k_harf=[]
b_harf=[]
while True:
    def harfsayisi(a): 
        for i in a:
            if i in kucuk_harfler:
                k_harf.append(i)
            elif i in buyuk_harfler:
                b_harf.append(i)
            else:
                continue
        return "Buyuk harf: {}, Kucuk harf: {}".format(len(b_harf),len(k_harf))

    veri=input("Lutfen bir metin giriniz cikis icin 'q':")
    if veri=='q':
        break
    print(harfsayisi(veri))
    
                
