def harfayıklayıcı(a):
    mlist=list(a)
    bharf=["A","B","C","D","E","F","G","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","W","Q","Z"]
    kharf=["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z","w","q"]
    ksayı=0
    bsayı=0
    print(mlist)
    for i in mlist:
        if i in bharf:
            bsayı+=1
        if i in kharf:
            ksayı+=1
            yazı="\nMetnin içinde {} adet büyük harf, {} adet küçük harf bulunmaktadır."
        
    return print(yazı.format(bsayı,ksayı))

while True:
    metin=input("\nMetni giriniz...:")
    harfayıklayıcı(metin)
    secim=input("Devam etmek için herhangi bir tuşa, çıkmak için q/Q tuşuna basınız...")
    if secim=="Q" or secim=="q":
        break
    
