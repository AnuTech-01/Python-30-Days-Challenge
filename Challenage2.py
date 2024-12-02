#CHALLENGE 2


Here is a simple example to demonstrate both:

#Example using *args:
 
def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1, 2, 3, 4, 5)

#Example using **kwargs:
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=25, city="New York")

def combined_example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

combined_example(1, 2, 3, name="Alice", age=25)
