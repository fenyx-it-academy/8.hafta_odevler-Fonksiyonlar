

def sesli_sessiz_sayisi(cumle):
    sesli_harfler = "aeıioöuüAEIİOÖUÜ"
    sessiz_harfler = "bcdfgğhjklmnprsştvyzBCDFGĞHJKLMNPRSŞTVYZ"

    sesli, sessiz, diger = 0, 0, 0
    for harf in cumle:
        if harf in sesli_harfler:
            sesli = sesli + 1
        elif harf in sessiz_harfler:
            sessiz = sessiz + 1
        else:
            diger = diger + 1
            
    
print ("Sesli harflerin sayısı : " ,sesli)
print ("Sessiz harflerin sayısı : " ,sessiz)
print ("Sesli-sessiz harflerin dışında girilen karakterlerin sayısı : ",diger)
