#CHALLENAGE 20

#Python RegEx

import re

# Function to validate an email address
def validate_email(email):
    # Regular expression for validating an email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Using re.match to check if the email matches the pattern
    if re.match(pattern, email): 
        return True
    else:
        return False

# Take user input for the email
email = input("Enter an email address: ")

# Validate the email and display the result
if validate_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
