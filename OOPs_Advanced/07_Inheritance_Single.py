# Single Inheritance in Python
# One child class inherits from one parent class.

class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        print("The dog barks.")

# Using the classes
dog = Dog()
dog.speak()  # Calls overridden method in Dog
