print("Please enter a number and see\nif it is *Prime Number* or Not!!")
while True:
    def primenum(number):
        for i in range(2,number):
            if number % i == 0:
                return "NOT a prime number"
            return "Is a prime number"
    print(primenum(int(input("Your number:\n "))))
