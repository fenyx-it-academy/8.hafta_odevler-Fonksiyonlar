# Verilen bir listenin içindeki özgün elemanları ayırıp
# yeni bir liste olarak veren bir fonksiyon yazınız.
# Örnek Liste : [1,2,3,3,3,3,4,5,5]
# Özgün Liste : [1, 2, 3, 4, 5]

def ozgunlist(a):
    list = []
    for i in a:
        if i not in list:
            list.append(i)
    return list

a = [1,2,2,4,1,4,1029,5,40,41,31,5,7,6,6,9,45,88]

print('Example list', a)
print("Unique list",sorted(ozgunlist(a)))