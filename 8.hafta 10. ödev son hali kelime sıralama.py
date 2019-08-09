def harfsıralama(a):
    metin=""        #çıktı verilecek olan metin
    kelime=""       #çıktı da yer alacak kelime
    degerliste=[]       #yazılan metinde her bir harfin alfebedik sıralamasından oluşan metin
    kod=[]                  #yazılan kelimelerin harflerinin alfabedik sıra numaralarından oluşan liste (kelime+kelime)
    kodtoplam=[]        #yazılan kelimelerin harflerinin alfabedik sıra numaralarından oluşan liste (tüm metin)
    harf=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","W","Q","X","Z","a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","w","q","x","z"]
    for i in a:         #metnin tüm harfleri sıra ile taranır
        if i in harf:           #harflerin sıra numaraları tespit edilir ve harf degeri olarak tanımlanır. sonra bu değerler degerlisteye eklenir
            if harf.index(i)<40:
                harfdeger=harf.index(i)
                degerliste+=[harfdeger]
            elif harf.index(i)>39:
                harfdeger=harf.index(i)-30
                degerliste+=[harfdeger]                
        else:
            harfdeger="-"
            degerliste+=[harfdeger]         #harf degerleri listesinde kelime aralarına - işareti konur

    for i in degerliste:            #harf degerlerinden oluşan listede "-" işaretine göre kelime grupları oluşturulur
        if i != "-":
            kod+=[i]
            #print(kod)
        else:
            kodtoplam+=[kod]
            kod=[]
    kodtoplam+=[kod]
    #print(degerliste)
    #print(kodtoplam)
    kodtoplam.sort()            #sort()  yardımı ile degerler listesi sayısal olarak listelenir
    ##print(kodtoplam)
    for i in kodtoplam:             #kodlar sayıların harf karşılıklarına göre tekrar kelimeye dönüştürülür
        for r in i:
            if r <10 or r>39:
                karakter=harf[r]
                kelime+=karakter
                
            elif 9<r<40:
                karakter=harf[r+30]             #kelime harflerinin tamamı küçük harfle yazılır
                kelime+=karakter
                
                
        metin+=kelime+"-"
        kelime=""
    print(metin)
    
while True:
    yazı=input("Lütfen sıralamak istediğini kelimeleri sadece harf ve rakam kullanıp aralarına '-' işareti koyarak yazınız\n")
    harf=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","W","Q","X","Z","a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","w","q","x","z"]
    for i in yazı:
        if i not in harf and i!="-":
            print("\nLütfen sadece harf ve rakamlardan oluşan kelimeler yazınız....\n")
            break
    
    harfsıralama(yazı)


        

