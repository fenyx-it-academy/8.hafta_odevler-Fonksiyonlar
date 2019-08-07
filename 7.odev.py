def pisegor():
    list=[]
    for i in range(1,101):
        for k in range(1,101):
            for j in range(1,101):
                if (i**2)+(k**2)==j**2:
                    list.append([i,k,j])

                    continue
                else:
                    continue
    listeson=[]
    listeson1=[]
    for k in range(0,len(list)-1):
        toplam=list[k][0]+list[k][1]+list[k][2]
        if toplam in listeson:
            pass
        else:
            listeson.append(toplam)
            listeson1.append([list[k][0],list[k][1],list[k][2]])

    return listeson1





print(pisegor())