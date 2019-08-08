print('b.')
'''
7-1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları 
ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
'''
def ozel_ucegen():
    ozel_ucgen_list=[]
    # for range ile 1-100 arasindaki sayilara baktik...ozel ucgen olusturan kenarlara bu sekilde baktik
    for kenar1 in range(1,101):
        for kenar2 in range(1,101):
            for hipotenus in range(1,101):
              if hipotenus**2==(kenar1**2+kenar2**2): #ozel ucgen olusturup olusturmadigini kontrolettik
                kenarlar=[kenar1,kenar2,hipotenus]  # sartlari olusturanlardan ayri bir liste olusturduk
                ozel_ucgen_list.append(kenarlar)    # ozellige uyanlari oz ucgen list ekledik
    return f"{ozel_ucgen_list}"
print(ozel_ucegen())