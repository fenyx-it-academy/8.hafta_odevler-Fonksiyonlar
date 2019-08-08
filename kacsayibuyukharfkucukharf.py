def sayiadet(kelime):
    return len([(i) for i in kelime if i.isdigit() == True])


def buyukharfadet(kelime):
    return len([(i)for i in kelime if i.isupper()==True])

def kucukharf(kelime):
    return len([(i) for i in kelime if i.islower()==True])


klm=input("bir metin giriniz:")

print(f"Bu metinde {sayiadet(klm)} adet sayi,{buyukharfadet(klm)} adet buyuk harf,{kucukharf(klm)} adet kucuk harf bulunmaktadir")


