list_original = [1,2,3,3,3,3,4,5,5]

def list_unique():
    list_1 = set(list_original)
    list_1 = list(list_1)
    return list_1

print(list_unique())