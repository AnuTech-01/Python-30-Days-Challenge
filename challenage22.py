#CHALLENAGE 22

#Python Polymorphism

# Base class
class Animal:
    def sound(self):
        pass

# Derived class Dog
class Dog(Animal):
    def sound(self):
        return "Woof....!"

# Derived class Cat
class Cat(Animal):
    def sound(self):
        return "Meow meow..!"

# Function to demonstrate polymorphism
def make_sound(animal: Animal):
    print(animal.sound())

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Polymorphic behavior
make_sound(dog) 
make_sound(cat)  
