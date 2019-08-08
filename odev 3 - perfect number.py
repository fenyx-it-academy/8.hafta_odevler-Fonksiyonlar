def divider(number):
    """ bir sayinin kendi haric tam bolenlerini veren fonksiyon"""
    int_number = []
    for i in range(1,number):
        if number % i == 0:
            int_number += [i]
    return int_number

def perfect_numbers(a):
    """ verilen sayiya kadar olan mukemmel sayilari liste halinde veren fonksiyon"""
    perfect_list=[]                 # bos liste tanimla
    for i in range(1,a):            # 1 den girdigimiz sayiya kadar dongu baslat
        if i == sum(divider(i)):    # dongudeki her sayiyinin kendisi haric tam bolenlerini bulup topla eger toplam kendisine esitse
            perfect_list+=[i]       # bos listeye ekle
    return perfect_list

print(perfect_numbers(1000))

