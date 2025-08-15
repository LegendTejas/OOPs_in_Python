# 4. Comparison Operator Overloading
# __eq__, __lt__, __gt__, etc.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

    def __lt__(self, other):
        return self.marks < other.marks

    def __gt__(self, other):
        return self.marks > other.marks

# Creating objects
s1 = Student("Alice", 85)
s2 = Student("Bob", 92)

print(s1 == s2)  # False
print(s1 < s2)   # True
print(s1 > s2)   # False
