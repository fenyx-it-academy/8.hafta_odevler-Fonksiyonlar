"""EBOB bulma"""
def ebob_bulma(sayi1,sayi2):
    ebob = []
    i =1#sayi1 ve sayi2 ye bolunebilen dongumuz
    while i<=sayi1 and i<=sayi2:#dongumuz her iki sayidan kucuk olacak sekilde devam etsin
        if sayi1%i == 0 and sayi2%i ==0:#her iki sayiya tam bolunebilen sayilarimizin ebobudur
            ebob.append(i)
        i+=1#degiskenimiz her dongude birer artiyor
    return ebob
sayi1 = int(input("sayi1 i giriniz: "))
sayi2  = int(input("sayi2 yi giriniz: "))
print("ebob:",ebob_bulma(sayi1,sayi2))