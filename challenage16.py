#CHALLENAGE 16

#Prime or not prime 

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Get user input
n= int(input("Enter a number: "))

# Check if the number is prime or not
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
