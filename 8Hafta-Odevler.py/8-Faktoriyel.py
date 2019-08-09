"""Faktoriyel Hesaplama"""
def faktoriyel(sayi):
    faktoriyel =1
    if sayi ==1 or sayi ==0:
        print("faktoriyel  :",faktoriyel)
    else:
        while sayi>=1:#sayi birden buyuk yada esitse dongu devam etsin
            faktoriyel*=sayi#her dongude degeri carpip faktoriyel degiskenine gonder
            sayi-=1#sayi her dongude bir azalsin
        print("faktoriyel: ",faktoriyel)
faktoriyel(4)