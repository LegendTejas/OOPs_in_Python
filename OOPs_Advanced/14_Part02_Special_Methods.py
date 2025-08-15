# 3. Arithmetic Operator Overloading
# __add__, __sub__, __mul__, etc.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

# Using overloaded operators
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(2, 2)
