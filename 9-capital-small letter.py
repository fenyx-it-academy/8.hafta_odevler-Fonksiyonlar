def capital(text):
    cap_counter = 0
    text = list(text)
    for let in text:
        if let.isupper() == True:
            cap_counter += 1
    return cap_counter
def sma_letter(text):
    sma_counter = 0
    text = list(text)
    for let in text:
        if let.islower() == True:
            sma_counter += 1
    return sma_counter
    
try:   
    print("*"*15,"SYSTEM OF COUNTING CAPITAL-SMALL LETTER","*"*15)
    text = input("Please enter your text:")
    for let in text:
        if let == " ":
            let = ""
    if let.isalpha() != True:
        print("Please enter letter")
    else:
        print(f"Your text has {capital(text)} capital and {sma_letter(text)} small letter") 
except:
    print("Error, please try again")
