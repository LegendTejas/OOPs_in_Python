# Methods in Python OOP
# Types of Methods:
# 1. Instance Method    → Works with object data (needs 'self')
# 2. Class Method       → Works with class data (needs 'cls', uses @classmethod)
# 3. Static Method      → Utility function, works independently (uses @staticmethod)

class School:
    # Class variable
    school_name = "Green Valley High School"

    def __init__(self, student_name, grade):
        # Instance variables
        self.student_name = student_name
        self.grade = grade

    # 1. Instance Method (accesses instance variables)
    def display_student_info(self):
        print(f"Student: {self.student_name}, Grade: {self.grade}")

    # 2. Class Method (accesses/modifies class variables)
    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
        print(f"School name changed to: {cls.school_name}")

    # 3. Static Method (utility method, doesn't access class or instance variables)
    @staticmethod
    def is_passing(score):
        return score >= 40

# Creating objects
student1 = School("Alice", "10th")
student2 = School("Bob", "9th")

# Instance method usage
student1.display_student_info()
student2.display_student_info()

# Class method usage
School.change_school_name("Blue Ridge Academy")

# Static method usage
print(f"Is 35 passing? {School.is_passing(35)}")
print(f"Is 75 passing? {School.is_passing(75)}")

"""
Output:
Student: Alice, Grade: 10th
Student: Bob, Grade: 9th
School name changed to: Blue Ridge Academy
Is 35 passing? False
Is 75 passing? True
"""

# Key points:
# - Instance methods: Work with object attributes.
# - Class methods: Work with class attributes and are marked with @classmethod.
# - Static methods: Independent utility functions, marked with @staticmethod.
