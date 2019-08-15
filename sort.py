#odev 10#
#sort#

print("girdiginiz kelimeleri alfabetik sıraya gore duzenleyecegız\n")
def sirala():
    kelime= input("Lutfen (-) ile ayirarak birden fazla kelime giriniz:")
    kelimeler=kelime.split("-")
    kelimeler.sort()
    print(*kelimeler,sep="-")

sirala()
