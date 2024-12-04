#CHALLENAGE 4
#Class and object

# Define a class called 'Person'
class Person:
    # Constructor to initialize the object's attributes
    def __init__(self, name, age):
        self.name = name  # Instance variable for name
        self.age = age    # Instance variable for age
    
    # Method to greet
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object (instance) of the Person class
person1 = Person("Anu", 19)

# Call the greet method on the object
person1.greet()

# Create another object
person2 = Person("divya", 19)
person2.greet()
