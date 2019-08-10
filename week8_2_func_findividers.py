def finddividers(num):
    dividerslist = []
    for i in range(1, num + 1):
        if (num % i == 0):
            dividerslist.append(i)
    return dividerslist



while True:
    num = input("\n\nEnter the number to find its dividers\n(Exit--> 'q'):.. ")

    if (num == "q" or num =="Q"):
        print("Exiting...")
        break
    else:
        num = int(num)
        fd = finddividers(num)
#        print(fd,"\n")
    for i in range(len(fd)-1):
        if i % 8 == 0:
            print("\n")
        print("{:<4}\t".format(fd[i]), sep="", end="")

