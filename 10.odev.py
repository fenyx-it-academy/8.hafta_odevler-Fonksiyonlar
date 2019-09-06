def terscevirme():
    enter=input("arasinda - birakarak kelimeleri yaziniz")
    liste=[]
    kucuk=[]
    kucuk=enter.split("-")
    kucuk.sort()
    print(kucuk)
    k=1
    for i in kucuk:
        liste.append(i)

        if k < len(kucuk):
            liste.append("-")
            k+=1

    print(*liste)


terscevirme()