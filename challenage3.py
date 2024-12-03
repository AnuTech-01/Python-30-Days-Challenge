#CHALLENAGE 3
#Lambda function

Here are some easy examples of Python lambda functions:

#Basic Lambda Function: A simple function to add two numbers.
add = lambda x, y: x + y
print(add(2, 3))


#Lambda with map(): Using a lambda function to square each number in a list.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

#Lambda with filter(): Using a lambda function to filter out even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  

#Lambda with sorted(): Sorting a list of tuples by the second element.
pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  

#Lambda in a List Comprehension: Using a lambda function to multiply each element in a list by 10.
numbers = [1, 2, 3, 4]
result = [lambda x: x * 10 for x in numbers]
print([r() for r in result])

#Lambda in reduce(): Using a lambda function to find the product of all numbers in a list (using functools.reduce).
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)

#Lambda to check for even or odd: A simple lambda to check if a number is even.
is_even = lambda x: x % 2 == 0
print(is_even(4))  
print(is_even(5))

#Lambda for String Manipulation: Convert a string to uppercase using lambda.
to_upper = lambda s: s.upper()
print(to_upper('hello'))  
