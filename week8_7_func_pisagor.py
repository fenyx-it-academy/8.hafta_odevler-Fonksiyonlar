# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana
# yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def find_pisagor():
    pisagor_List = list()
    for pisg in range(1, 101):
        for j in range(1, 101):

            c = (pisg ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pisagor_List.append((pisg, j, int(c)))

    return pisagor_List


for pisg in find_pisagor():
    print(pisg, end=" ")
