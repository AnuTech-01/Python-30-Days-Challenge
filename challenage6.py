#CHALLENAGE 6

# Simple program to divide two numbers with error handling

try:
    # Take user input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Try to divide the numbers
    result = num1 / num2
    print(f"The result of division is: {result}")

except ZeroDivisionError:
    # Handle division by zero error
    print("Error: You cannot divide by zero!")

except ValueError:
    # Handle invalid input (non-numeric values)
    print("Error: Please enter valid numbers.")

except Exception as e:
    # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
