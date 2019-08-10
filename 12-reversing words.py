def reverse(word):
    let_list = []
    new_let_list = []

    for letter in word:
        if letter == " ":
            letter = ""
            
    new_word = reversed(letter)
    for let in new_word:
        new_let_list += [let]
    for let in letter:
        let_list += [let]
    if let_list == new_let_list:
        return True
    return False
try:
    print("*"*15, "REVERSING WORDS", "*"*15)
    word = input("Please enter your word whether to check its reversed situation is the same its original situation:")
    print(reverse(word))
except:
    print("Error, please try again")
