def ters(*metin):
    tersi=metin[:-1]
    true=[]
    false=[]
    for i in tersi:
        for z in metin:
            if i==z:
                true.append(i)
    for i in true:
        print(f'{i}=True')
    for i in metin:
        if i not in tersi:
            false.append(i)
    for i in false:
        print(f'{i}=False')
ters('madam','taco cat','utrecht')
