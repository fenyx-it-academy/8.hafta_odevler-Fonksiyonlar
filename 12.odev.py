'''
12-Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız.
 örnek: madam, taco cat, utrecht sonuç: True, True, False
'''

def fonk(*args):                                # fonk adında birden fazla argümant olabilen fonksiyon oluşturduk
  durum=" "                                     # durumları atmak için string tanimladik.
  for i in args:                                # args tuple üzerinde değerlerini donduruyoruz.
    if i== i[::-1]:                             # eğer değer ile tersi eşitse duruma True ekliyoruz.
       durum+="True"
    else:                                       # değilse duruma False ekliyoruz.
      durum+="False"
  return durum

print(fonk("madam","tacocat","utrecht"))
