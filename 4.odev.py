'''
4-Kullanıcıdan 2 tane sayı alarak
 bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
'''

def ebob_bulma(a,b):

    ebob = []
    i = 1 # a ve b ye bölünebilen sayılar

    while i <= a and i <= b: # dögüler parametrelerimizden küçük olacak bölüm için
        if a%i == 0 and b%i == 0: # her iki sayıya tam bölünebilen sayıların ebobu
            ebob.append(i)
        i+=1
    return ebob
a = int(input("ilk sayıyı giriniz: "))
b = int(input("ikinci sayıyı giriniz: "))
print("ebob:", ebob_bulma(a,b))
