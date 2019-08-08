
def reverse_comp():
    while True:
        word = input("Karsilastiracaginiz Kelimeyi giriniz(sonlandirmak icin q tusuna basiniz) : ")
        if word=="q":
            break
        elif word==word[::-1]:
            print(True)
        else:
            print(False)
reverse_comp()
