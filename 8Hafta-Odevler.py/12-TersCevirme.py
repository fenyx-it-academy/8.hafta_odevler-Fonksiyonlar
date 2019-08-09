"""Verilen inputların tersten de aynı olup olmadığını kontrol eden bir fonksiyon yazınız.örnek: madam, taco cat, utrecht sonuç: True, True, False"""
def terscevir(s):
    if s[::-1]:#aldigimiz inputu ters cevirmissek True degilse False degeri donsun
        return True
    else:
        return False
while True:
    try:
        s = input("ters cevirmek istediginiz ifadeyi yazininz: ")

        print(terscevir(s))
    except:
        print("bir hata olustu")

