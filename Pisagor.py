def pisagor():
    pisagor=[]
    for i in range(1,101):
        for j in range(1,101):
            c=(j**2+i**2)**0.5
            if c==int(c):
                pisagor.append([i,j,int(c)])
    for i in pisagor:
        print(i)
pisagor()
