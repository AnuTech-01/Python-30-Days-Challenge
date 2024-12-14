#CHALLENAGE 12

#Python Functions 

# Function to print a greeting message
def greet(name):
    print(f"Hello, {name}!")

# Function to calculate the sum of two numbers
def add(a, b):
    return a + b

# Function to check if a number is even or odd
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Call the functions
greet("Anu")  # Output: Hello, Alice!
result = add(10, 20)  # Adds 10 and 20
print(f"The sum is: {result}")  # Output: The sum is: 30

number = 22
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
