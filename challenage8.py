#CHALLENAGE 8

'''# 1. math modules
import math

# Calculate square root
print(math.sqrt(16))  

# Calculate factorial
print(math.factorial(5))

# Trigonometric functions
print(math.sin(math.pi / 2))  

# 2. random
import random

# Random integer between 1 and 100
print(random.randint(1, 100))  

# Random choice from a list
colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))  

# Shuffle a list
random.shuffle(colors)
print(colors)

# 3. time module
import time

# Get current time
current_time = time.localtime()
print(time.strftime("%H:%M:%S", current_time))  

# Sleep for 2 seconds
print("Waiting for 2 seconds...")
time.sleep(2)
print("Done waiting.")'''

# 4. os module
import os

# Get the current working directory
print(os.getcwd())  

# List files and directories in the current directory
print(os.listdir())

# 5. datetime module
'''import datetime

# Get current date and time
now = datetime.datetime.now()
print(now)  

# Get only the date
print(now.date())  

# Get the day of the week
print(now.strftime("%A"))

# 6. requests module
import requests

# Make a simple GET request to a website
response = requests.get('https://www.example.com')

# Check if the request was successful
if response.status_code == 200:
    print("Request successful!")
    print("Response content:", response.text[:200])  
    else:
    print(f"Request failed with status code {response.status_code}")


# 7. json module
import json

# Convert Python dictionary to JSON string
data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_string = json.dumps(data)
print(json_string)

# Parse JSON string into Python dictionary
parsed_data = json.loads(json_string)
print(parsed_data)'''



 




