#CHALLENAGE 18

#Python Numbers:

# Python program for basic number operations

# Input: Getting two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Output: Display the results
print(f"The sum of {num1} and {num2} is: {addition}")
print(f"The difference between {num1} and {num2} is: {subtraction}")
print(f"The product of {num1} and {num2} is: {multiplication}")
print(f"The division of {num1} by {num2} is: {division}")
