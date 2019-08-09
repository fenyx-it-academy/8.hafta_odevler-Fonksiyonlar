# coding=utf-8
def sıralı_kelime(veri):
    #fonksiyon ve paremetre tanımlama
    liste=veri.split('-')
    #veriyi - isaretinden bolup listeye donusturme
    liste.sort()
    #listenin verilerini sıralama
    for i in range(len(liste)-1):
        # liste uzunlugunun bir eksigi sayıda dongu
        liste[i]+=' -'
        # listenin elemanları arasına '-' isaretini eleman olarak atama
    print (*liste)
    #liste elemanlarını yazdırma

