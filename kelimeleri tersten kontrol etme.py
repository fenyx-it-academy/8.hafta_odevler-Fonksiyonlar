#Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız.
# örnek: madam, tacocat, utrecht sonuç: True, True, False

def ters_metin(metin):    #buraya input verirseniz ve asagidaki fonk. silerseniz
                          # kelime kelime kontrol eder

    if metin==metin[::-1]:#verilen metni ters cevirir
        return True
    else:
        return False

def coklu_ters_metin(metin_2=input("Kelimeleri ',' ile ayirin :")):
    goster=[]               #girilen metinleri listeye atiyoruz
     #split()fonksiyonu ile listeye donusturduk
    for sayac in metin_2.split(','):
        goster+=[ters_metin(sayac)] #buraya dikkat edelim metindeki herbir deger bir onceki fonksiyonda
                                    #islem goruyor true false degeri olarak donuyor
    return  goster

print(*coklu_ters_metin())
