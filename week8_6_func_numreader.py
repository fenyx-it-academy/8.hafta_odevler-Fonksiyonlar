"""Kullanıcıdan 2 basamaklı bir number alın ve bu numbernın okunuşunu
 bulan bir fonksiyon yazın. Örnek: 97 ---------> Doksan Yedi"""
import time
ones = ["", "Bir", "İki", "Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]

tens = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def digitreader (number):
    firstdigit  = number %  10
    seconddigit = number // 10

    return tens [seconddigit]+ones[firstdigit]
print("__Simple Number Reader__\n"
      "Type A Number Betweeen 1-99\n"
      "0--»exit \n")
while True:
    number = int(input("Pls enter your number: "))

    if number == 0:
        print("Görüşmek üzere, prg sonlandırılıyor!!")
        time.sleep(1)
        quit()


    elif number < 0 or number > 99:
        print("Enter a number between 0-99")
        continue

    else:
        print("--»", digitreader(number))