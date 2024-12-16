# CHALLENAGE 15

#Palindrome Number

def is_palindrome(number):
    # Convert the number to a string
    str_number = str(number)
    
    # Check if the string is equal to its reverse
    if str_number == str_number[::-1]:
        return True
    else:
        return False

# Input number from user
num = int(input("Enter a number: "))

# Check if the number is palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
