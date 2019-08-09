def asal(sayi):
    if sayi==1 :
        print('1 asal sayi degildir!')
        quit()
# try :
    sayac=0
#for dongusu ile kullanicidan aldigimiz asal sayiyi range yardmiyla
#2'den o sayiya kadar butun sayilari bolduk bunlarin icinde
#herhangi biri ile tam bolunmesi durumunda sayinin asal olmadigi
#eger bolunmuyorsa sayinin asal oldugu ciktisini verdik
    for i in range(2,sayi):
        if sayi%i==0:
            sayac+=1
            break
    if sayac!=0:
        print(f'{sayi}  asal sayi degildir!')
    else :
       print(f'{sayi}  asal sayidir')
# except NameError :
#     print('lutfen sadece sayi giriniz')
asal(5)
#donguye karakter girmesi durmunda hata mesaji verdirmeye calistim
#ama olmadi onu ileride belki duzletebilirm diye boyle birakiyorum