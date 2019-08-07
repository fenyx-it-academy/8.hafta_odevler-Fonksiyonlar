print(14 * " >", "\t n.B.a. \t", "< " * 14, "\n\n\n")

def pis_agor(*args):
    liste = []
    count = 0
    for i in range(1, 101):
        for j in range(1, 101):
            for k in range(1, 101):
                if k**2 == (i**2 + j**2):
                    uclu_liste = [i, j, k]
                    liste.append(uclu_liste)
                    count += 1
    return print(f"There are {count} Pythagorian triple and list is:\n", liste)


pis_agor()
