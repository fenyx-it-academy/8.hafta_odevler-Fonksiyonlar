print("********** Pythagorous' Triangle **********\n\n")
def pythagorous(args):
    empty=[]
    for x in range(1,args):
        for y in range(1,args):
            for z in range(1,args):
                if x<y and pow(z,2)==pow(x,2)+pow(y,2):
                    empty+=[(x,y,z)]
    return print(*empty)
pythagorous(100)

                    
