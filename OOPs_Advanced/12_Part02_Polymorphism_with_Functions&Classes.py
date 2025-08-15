# Polymorphism with Common Interface
# Different objects can be passed to the same function if they have the same method.

class Car:
    def fuel_type(self):
        return "Petrol"

class ElectricCar:
    def fuel_type(self):
        return "Electric"

def show_fuel(vehicle):
    print(f"Fuel Type: {vehicle.fuel_type()}")

# Passing different objects to the same function
show_fuel(Car())
show_fuel(ElectricCar())
