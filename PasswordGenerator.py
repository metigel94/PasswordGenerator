import random
import string

lowerCase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperCase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
specialChars = ['!', '§', '$', '&', '/', '(', ')', '=', '?', 'ß', '´', '|']

def passwordGen(length, complexity):
    i = 0
    password = []
    finalPassword = ''
    while i < length:
        comp = random.randrange(complexity)

        if comp == 0:
            password.append(lowerCase[random.randrange(25)]) 
        if comp == 1:
            password.append(upperCase[random.randrange(25)]) 
        if comp == 2:
            password.append(specialChars[random.randrange(10)])
               
        i += 1
    
    for letters in password:
        finalPassword += letters
    
    print("Your new Password is: " + finalPassword)


userLength = input("How long should your Password be? Please enter a number: ")
userComplexity = input("How complex should your password be? 1 = lower-case only. 2 = lower-case and upper-case. 3 = lower-case, upper-case and special characters. Please enter a number: ")
passwordGen(int(userLength), int(userComplexity))