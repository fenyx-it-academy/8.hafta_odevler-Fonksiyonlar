def authentic(lst):
    lst = set(lst)
    lst = list(lst)
    return lst

print(authentic([1,2,2,2,3,4,4,4,5,5,"AA","aa","aa"]))
