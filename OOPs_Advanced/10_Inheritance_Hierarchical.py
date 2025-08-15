# Hierarchical Inheritance in Python
# Multiple child classes inherit from the same parent class.

class Vehicle:
    def start_engine(self):
        print("Engine started.")

class Car(Vehicle):
    def drive(self):
        print("Driving the car.")

class Bike(Vehicle):
    def ride(self):
        print("Riding the bike.")

# Using the classes
car = Car()
car.start_engine()
car.drive()

bike = Bike()
bike.start_engine()
bike.ride()
