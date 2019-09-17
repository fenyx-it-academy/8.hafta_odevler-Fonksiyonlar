def ters():
    girdi=input("'-' ile ayrılan bir liste olusturunuz: ")
    girdi=girdi.split("-")
    girdi.sort()
    print( *girdi,sep="-")
ters()
