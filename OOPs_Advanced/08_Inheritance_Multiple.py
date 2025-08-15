# Multiple Inheritance in Python
# A child class inherits from more than one parent class.

class Father:
    def skills(self):
        print("Father: Knows driving.")

class Mother:
    def skills(self):
        print("Mother: Knows cooking.")

class Child(Father, Mother):  # Inherits from both Father and Mother
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Child: Knows coding.")

# Using the class
child = Child()
child.skills()
