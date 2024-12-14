# Base class (Parent class)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Some generic animal sound"
#CHALLENAGE 13

#Python Inheritance

# Derived class (Child class)
class Dog(Animal):
    def __init__(self, name, breed):
        # Calling the constructor of the parent class
        super().__init__(name, "Dog")
        self.breed = breed

    # Overriding the speak method from the parent class
    def speak(self):
        return f"{self.name} says Woof!"

# Another derived class (Child class)
class Cat(Animal):
    def __init__(self, name, color):
        # Calling the constructor of the parent class
        super().__init__(name, "Cat")
        self.color = color

    # Overriding the speak method from the parent class
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of the child classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "white")

# Calling methods from the parent and child classes
print(f"{dog.name} is a {dog.species} of breed {dog.breed}.")
print(dog.speak())  # Output: Buddy says Woof!

print(f"{cat.name} is a {cat.species} of color {cat.color}.")
print(cat.speak())  # Output: Whiskers says Meow!
