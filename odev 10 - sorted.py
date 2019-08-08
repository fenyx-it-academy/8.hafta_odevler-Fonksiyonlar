
def ranking(a):
    b = a.split("-")
    b=sorted(b)
    b="-".join(b)
    return b

print(ranking("green-red-yellow-black-white"))