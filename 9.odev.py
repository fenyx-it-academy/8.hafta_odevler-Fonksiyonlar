def buyukkucukharf():
    enter=input("Lutfen bir kelime giriniz")
    buyuk=[]
    kucuk=[]
    sayi=[]
    others=[]
    for i in enter:
        print(i)
        if i.isupper()==True:
            buyuk.append(i)
        if i.islower()==True:
            kucuk.append(i)
        if i.isdigit()==True:
            sayi.append(i)
        if i.isalnum()==False:
            others.append(i)
    print("buyuk harfler {} olusmakta olup {} tanedir".format(buyuk,len(buyuk)))
    print("kucuk harfler {} olusmakta olup {} tanedir".format(kucuk,len(kucuk)))
    print("rakamlar {} olusmakta olup {} tanedir".format(sayi,len(sayi)))
    print("diger karekterler {} olusmakta olup {} tanedir".format(others, len(others)))
    
buyukkucukharf()