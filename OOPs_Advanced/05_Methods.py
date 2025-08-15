# Instance Variables vs Class Variables in Python

class Employee:
    # Class variable (shared across all instances)
    company_name = "TechCorp"

    def __init__(self, name, salary):
        # Instance variables (unique for each object)
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company_name}")

# Creating objects
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

# Accessing instance and class variables
emp1.display_info()
emp2.display_info()

# Changing class variable
Employee.company_name = "CodeMasters"

print("\nAfter changing class variable:")
emp1.display_info()
emp2.display_info()

# Changing instance variable for one object
emp1.salary = 55000
print("\nAfter changing instance variable for emp1:")
emp1.display_info()
emp2.display_info()

"""
Output:
Name: Alice, Salary: 50000, Company: TechCorp
Name: Bob, Salary: 60000, Company: TechCorp

After changing class variable:
Name: Alice, Salary: 50000, Company: CodeMasters
Name: Bob, Salary: 60000, Company: CodeMasters

After changing instance variable for emp1:
Name: Alice, Salary: 55000, Company: CodeMasters
Name: Bob, Salary: 60000, Company: CodeMasters
"""

# Key points:
# - Class variables are shared by all objects (change affects all instances).
# - Instance variables are unique for each object (change affects only that object).
# - Access class variables using the class name for clarity.
