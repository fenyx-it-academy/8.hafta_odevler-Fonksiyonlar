# Kullanıcıdan bir input alan ve bu inputun içindeki
# büyük ve küçük harf sayılarının veren bir fonksiyon yazınız.

def lettercount(word):
    smalletter = 0
    capitalletter=0

    for i in word:
        if i.islower()==True:
            smalletter+=1
        elif i.isupper()==True:
            capitalletter+=1
    return f"{smalletter} smalletter(s) and {capitalletter} capitalletter(s)"
a=input("Enter your word\n")
print(lettercount(a))
