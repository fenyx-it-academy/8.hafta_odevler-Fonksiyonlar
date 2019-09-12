print('b.')
'''
>>>>>>>>>>>>>>>>>>>>>>> ters duz <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

12-Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız.
örnek: madam, tacocat, utrecht sonuç: True, True, False
'''
def terside_ayni(*args):
    veri=input("Lutfen kelimelerinizi aralarina ',' koyarak giriniz giriniz: ")
    duz_liste=[]                            # duz diye bos liste olusturduk
    for i in veri.split(','):
        duz_liste.append(i)                 # girilen verileri duz listemize ekledik
    kontrol_listesi=[]
    for duz in duz_liste:
        ters= duz[::-1]                     #  [::-1] kelimemizi ters cevirdik
        print(ters)
        if duz==ters:                       # if ile duz sekli tersine esit mi diye kontrol ettik
            kontrol_listesi.append(True)
        else:
            kontrol_listesi.append(False)
    return kontrol_listesi

print(terside_ayni())
