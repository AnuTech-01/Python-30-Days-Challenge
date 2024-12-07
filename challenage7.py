# Simple program to demonstrate array (list) operations

#CHALLENAGE 7

# Create an array (list) of numbers
numbers = [1, 2, 3, 4, 5]

# Print the original array
print("Original array:", numbers)

# Add a number to the array
numbers.append(6)
print("Array after appending 6:", numbers)

# Remove a number from the array
numbers.remove(3)
print("Array after removing 3:", numbers)

# Access an element by index
print("Element at index 2:", numbers[2])

# Iterate through the array and print each element
print("Iterating through the array:")
for num in numbers:
    print(num)

# Find the length of the array
print("Length of the array:", len(numbers))

# Sort the array
numbers.sort()
print("Sorted array:", numbers)

# Reverse the array
numbers.reverse()
print("Reversed array:", numbers)
