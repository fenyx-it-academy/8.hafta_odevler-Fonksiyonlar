####################################################################################

print("EBOB hesaplama")
def ebobhes(x,y):
    ortliste=[]
    if x<y:
        for i in range(1,y):
            if x%i==0 and y%i==0:
                ortliste.append(i)
    elif y<x:
        for i in range(1,x):
            if x%i==0 and y%i==0:
                ortliste.append(i)
    print(ortliste)
    ebob=1
    for i in ortliste:
        ebob*=i
    print("EBOB",(x,y),"=",i)

try:
    x = int(input("lutfen Ebobunu bulmak istediginiz ilk sayiyi giriniz:"))
    y = int(input("lutfen Ebobunu bulmak istediginiz ikinci sayiyi giriniz:"))
except ValueError:
    print("Lutfen Sayisal degerler giriniz.")
if x==0 or y==0:
    raise BaseException("Lutfen sifirdan farkli sayilar giriniz.")
ebobhes(x,y)


###############################################################
print("EKOK hesaplama")
def ekokhes(x,y):
    kume=set()
    xlist=[]
    ylist=[]
    control=[]
    carpim=1
    i=2
    while i<=max(x,y):
        if x%i==0:
            x//=i
            xlist.append(i)
            kume.add(i)
        elif x==1:
            break
        else:
            i+=1
    a=2
    while a<=max(x, y):
        if y % a == 0:
            y //= a
            ylist.append(a)
            kume.add(a)
        elif a==1:
            break
        else:
            a += 1
    print("x'in bolenleri=", xlist)
    print("y'nin bolenleri=",ylist)
    print("ortak kume=",kume)
    for i in kume:
        if i in control:
            continue
        elif xlist.count(i)>ylist.count(i):
            control.append(i)
            carpim*=i**xlist.count(i)
        elif xlist.count(i)<ylist.count(i):
            control.append(i)
            carpim *= i ** ylist.count(i)
    return carpim
while True:
    a = int(input("lutfen Ekokunu bulmak istediginiz ilk sayiyi giriniz:"))
    b = int(input("lutfen Ekokunu bulmak istediginiz ikinci sayiyi giriniz:"))
    print(ekokhes(a,b))
