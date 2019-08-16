#bu kod tireler ile ayrilmis elemanlari alfabetik siraya gore siralar

liste=input("listenin elemanlarini aralarina - koyarak girin:")  #kullanicidan liste elemanlari ister

liste=liste.split('-')              #tire yardimiyla elemanlar tek tek listenin elemani haline getirir

liste=sorted(liste)         #liste elemanlari siralar
liste="-".join(liste)       #liste elemanlari tirelerle birlestirilerek string yapar


print(f"{liste} verilerin siralanmis halidir hali")
