"""

    ASSIGNMENT #1
    QUESTION 4
    AUTHOR: Bonnie Ives de Castro Nunes
    DATE: September 15th, 2023
    
"""

print("Please inform the string: ")
myString = input()

stringLength = len(myString)

print("\n------------------------------")
print("Please inform the number of characters you want to remove: ")
number = input()

if int(number) > stringLength:
    print("\n------------------------------")
    print("You want to remove " + number + " characters from a " + str(stringLength) + " character string.")

elif int(number) == stringLength:
    print("\n------------------------------")
    print("You removed all the characters from the string.")

else:

    letter = [char for char in myString]

    counter = 0
    for character in range(0,int(number)):
        letter.pop(0)
    
    print("\n------------------------------")
    print("Remainder letters after removing the first " + number + " characters.")
    print(letter)
        
