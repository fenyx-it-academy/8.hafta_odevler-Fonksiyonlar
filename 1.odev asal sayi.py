##Verilen sayinin asal sayi olup olmadigin bulma.
sayi=int(input("Bir sayi giriniz: "))
sayac=0
def asal_sayi(sayi):
## sayac i def disinda kullanabilmek icin global kullandik          
      global sayac                    
      for i in range(2,int(sayi)):        
            if sayi % i == 0:
                  sayac+=1
                  print("Sayı Asal Değil")
#return: Elde edilen fonksiyonun def haricindede kullanilmasini saglar
                  return(sayi)            
            else:
                  print("Sayı Asal")
                  return(sayi)
#bu ifadeyi yazmayinca sonuc vermiyor    
asal_sayi(sayi)           
