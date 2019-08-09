def ranking():
    words=input("Enter words with (-) sign between them ")
    order=[]
    order=letter.split("-")
    order.sort()
    return print(*order, sep="-")
ranking()
