def reading(number):
    numbers = {"1":"one", "2":"two" ,"3":"three", "4":"four", "5":"five",
               "6":"six", "7":"seven", "8":"eight" ,"9":"nine"}
    reading = {"10":"ten", "11":"eleven",
               "12":"twelve", "13":"thirteen", "14":"fourteen", "15":"fifteen",
               "16":"sixteen", "17":"seventeen", "18":"eighteen",
               "19":"nineteen"}
    decade = { "20":"twenty", "30":"thirty", "40":"forty",
               "50":"fifty", "60":"sixty", "70":"seventy", "80":"eighty",
               "90":"ninety"}
    if number in reading.keys():
        text = reading[number]
        return text
    if number in decade.keys():
        text = decade[number]
        return text
    for num in decade.keys():       
        if num[0] == number[0]:     #to check that the number's first item is in decade number
            new_number = number[0] + "0"    #set 'new_number' because we can only check decade numbers 
            text = decade[new_number]       #(like 30) and we haven't got decade numbers (like 32)
    if number[1] in numbers.keys():     #check number's second item in order to add reading of number
        text += numbers[number[1]]      
        return text

print("*"*15,"READING NUMBER","*"*15)
try:
    while True:
        number = input("Please enter number between 10-99 which will be read:")
        if len(number) != 2 or number.isdigit() != True:
            print("\nPlease enter number between 10-99\n")
        else:
            print(f"\n------>{reading(number)}")
            break
except:
    print("Error, please try again")
