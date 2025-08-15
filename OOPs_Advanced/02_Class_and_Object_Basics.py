# Class & Object Basics in Python

# A class is a blueprint for creating objects.
# An object is an instance of a class.

class Person:
    # Class attribute (shared by all objects)
    species = "Homo sapiens"

    # Instance attributes (unique for each object)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to introduce the person
    def introduce(self):
        print(f"Hi, I'm {self.name} and I am {self.age} years old.")

# Creating objects (instances) of Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing instance methods
person1.introduce()
person2.introduce()

# Accessing class attribute
print(f"All humans belong to species: {Person.species}")

# Accessing attributes directly
print(f"{person1.name} is {person1.age} years old.")
print(f"{person2.name} is {person2.age} years old.")

"""
Output:
Hi, I'm Alice and I am 25 years old.
Hi, I'm Bob and I am 30 years old.
All humans belong to species: Homo sapiens
Alice is 25 years old.
Bob is 30 years old.
"""

# Key points:
# - Class attribute: Same for all instances.
# - Instance attribute: Unique for each instance.
# - Objects are created by calling the class like a function.
# - Methods define behaviors for the objects.
