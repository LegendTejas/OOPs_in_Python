# Partial implementation in abstract classes
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color  # Common attribute for all shapes

    @abstractmethod
    def area(self):
        pass

    def describe(self):  # Concrete method
        print(f"This is a {self.color} shape.")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Using the class
rect = Rectangle("blue", 5, 3)
rect.describe()
print(f"Area of rectangle: {rect.area()}")
