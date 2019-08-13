def siralama():
    color_final=""
    colors=input("Lutfen renkleri giriniz : ")
    colors_each=colors.split("-")
    colors_each.sort()
    for i in colors_each:
        color_final+=i + "-"
        final=color_final.rstrip(color_final[-1])
    return final

print(siralama())