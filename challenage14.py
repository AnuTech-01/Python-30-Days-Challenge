#CHALLENAGE 14

#Fibonacci Number

# Function to generate Fibonacci sequence up to 'n' terms
def fibonacci(n):
    # Starting values of the Fibonacci sequence
    a, b = 0, 1
    
    # Loop to generate the Fibonacci numbers
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update the values of a and b

# Example usage
n = 10  # Number of terms
fibonacci(n)
