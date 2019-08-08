print('b.')
'''
>>>>>>>>>>>>>>>>>>>>>>> ters duz <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

12-Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız.
örnek: madam, tacocat, utrecht sonuç: True, True, False
'''
def terside_ayni():
    veri=input("Lutfen Herhangi bir kelime giriniz: ")
    # ters duz diye bos liste olusturduk
    duz=[]
    ters=[]
    for i in veri:
        duz.append(i)       # veriyi duz listemize ekledik
    for k in veri[::-1]:    # veri[::-1] veriyi ters cevirdik
        ters.append(k)      # ters cevrilen veriyi ters listemize ekledik
    if duz==ters:           # if ile duz sekli tersine esit mi diye kontrol ettik
        return True
    return False
print(terside_ayni())
