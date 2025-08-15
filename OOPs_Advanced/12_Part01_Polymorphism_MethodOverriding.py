# Polymorphism with Method Overriding
# Same method name, different implementations in parent & child classes.

class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()  # Calls the version based on object type
