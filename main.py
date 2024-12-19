# Input and Prints
# Task 1:
"""
Create a program that asks the user for their name and favorite programming language,
then prints a message like:
    Hello [Name], you love [Language]!
"""

print("Task 1.")
name = input("Enter your name: ")
favoriteLanguage = input("Enter your favorite programming language: ")
print(f"Hello {name}, you love {favoriteLanguage}!")

# Task 2:
"""
Write a program that asks the user to input two numbers
and outputs their sum and difference in the format:
The sum of [num1] and [num2] is [sum].
The difference between [num1] and [num2] is [difference].
"""

print("\nTask 2.")
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
print(f"The sum of {firstNumber} and {secondNumber} is {firstNumber + secondNumber}.")
print("AND")
print(f"The difference between {firstNumber} and {secondNumber} is {firstNumber - secondNumber}.")

# Numbers and Arithmetic Operations
# Task 3:
"""
Create a program that calculates the area of a rectangle.
Ask the user to input the length and width,
then calculate and display the area as:
"""

print("\nTask 3.")
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
print(f"The area of the rectangle is {length * width}.")

# Task 4:
"""
Write a program that takes an integer input from the user
and checks whether it is divisible by 3 and 5.
Print:
    [Number] is divisible by 3 and 5.
Or:
    [Number] is not divisible by 3 and 5.
"""

print("\nTask 4.")
userInput = int(input("Enter a number: "))
if userInput % 3 == 0 and userInput % 5 == 0:
    print(f"{userInput} is divisible by 3 and 5.")
else:
    print(f"{userInput} is not divisible by 3 and 5.")

# Strings and Lists
# Task 5:
"""
Ask the user to input a sentence. Convert the sentence to uppercase
and count the number of words in it. Display the result as:
The sentence in uppercase: [UPPERCASE_SENTENCE]
Number of words: [WORD_COUNT]
"""

print("\nTask 5.")
sentence = input("Enter a sentence: ")
print(f"Sentence in uppercase: {sentence.upper()}")
print(f"Number of words: {len(sentence.split())}")

# Task 6:
"""
Write a program that creates a list of 5 favorite fruits entered by the user.
Then display the list in reverse order:
Your favorite fruits in reverse order: [fruit5, fruit4, ..., fruit1]
"""

print("\nTask 6.")
fruit1 = input("Enter your favorite fruit 1: ")
fruit2 = input("Enter your favorite fruit 2: ")
fruit3 = input("Enter your favorite fruit 3: ")
fruit4 = input("Enter your favorite fruit 4: ")
fruit5 = input("Enter your favorite fruit 5: ")
favoriteFruits = [fruit5, fruit4, fruit3, fruit2, fruit1]
print(f"Your favorite fruits in reverse order: {favoriteFruits}")

# Conditionals
# Task 7:
"""
Ask the user to enter their age and check if they are eligible to vote.
If the age is 18 or older, display:
    You are eligible to vote.
Otherwise:
    You are not eligible to vote.
"""

print("\nTask 7.")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Task 8:
"""
Write a program that asks the user for a number and checks
if it is positive, negative, or zero. Display:
    The number [number] is positive.
Or:
    The number [number] is negative.
Or:
    The number is zero.
"""

print("\nTask 8.")
number = int(input("Enter a number: "))
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
elif number == 0:
    print("The number is zero.")

# Loops
# Task 9:
"""
Create a program that prints all even numbers
between 1 and a number entered by the user.
Display them as:
    Even numbers from 1 to [number]: [2, 4, 6, ...]
"""

print("\nTask 9.")
number = int(input("Enter a number: "))
evens = []
for i in range(1, number + 1): # starting from 1 so that evens won't include zero
    if i % 2 == 0:
        evens.append(i)
    i += 1
print(f"Even numbers from 1 to {number}: {evens}")

# Task 10:
"""
Write a program that calculates the factorial of a number
entered by the user using a while loop.
Display the result as:
    The factorial of [number] is [factorial].
"""

print("\nTask 10.")
number = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"The factorial of {number} is {factorial}.")
