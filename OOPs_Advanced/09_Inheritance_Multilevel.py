# Multilevel Inheritance in Python
# A child inherits from a parent, and another child inherits from that child.

class Grandparent:
    def house(self):
        print("Grandparent: Owns a farmhouse.")

class Parent(Grandparent):
    def car(self):
        print("Parent: Owns a sedan.")

class Child(Parent):
    def bike(self):
        print("Child: Owns a sports bike.")

# Using the classes
c = Child()
c.house()  # From Grandparent
c.car()    # From Parent
c.bike()   # From Child
