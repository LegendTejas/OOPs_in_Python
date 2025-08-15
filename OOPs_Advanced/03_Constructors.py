# Constructors in Python

# A constructor is a special method that runs automatically
# when a new object of a class is created.
# In Python, the constructor method is __init__.

class Student:
    def __init__(self, name="Unknown", age=0):  # Constructor with default values
        self.name = name
        self.age = age
        print(f"Student object created for {self.name}")

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects with parameters (Parameterized Constructor)
student1 = Student("John", 21)
student1.show_details()

# Creating objects without parameters (Default Constructor behavior)
student2 = Student()
student2.show_details()

"""
Output:
Student object created for John
Name: John, Age: 21
Student object created for Unknown
Name: Unknown, Age: 0
"""

# Key points:
# - __init__ is called automatically when an object is created.
# - You can provide default values for flexibility.
# - Used to initialize attributes of an object.
