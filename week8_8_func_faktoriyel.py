import time
def faktoriyel(number):
    try:
        no=1
        for i in range(2, number+1):
            no*=i
        return print(f'Faktoriyel--» {number} =',no)
    except:
        return print('Pls enter a number!')

print("Faktöriyel Finder")
while True:
    a=input("Enter your number, 0--» exit: ")
    if a == "q":
        print("Görüşmek üzere, prg sonlandırılıyor!")
        time.sleep(1)
        quit()
    else:
        a=int(a)
        faktoriyel(a)