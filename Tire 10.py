def ranking():
    words=input("Enter words with (-) sign between them ")
    order=[]
    order=words.split("-")
    order.sort()
    return print(*order, sep="-")
ranking()
