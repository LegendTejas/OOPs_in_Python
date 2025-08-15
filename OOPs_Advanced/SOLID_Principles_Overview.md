# SOLID Principles Overview

The **SOLID principles** are a set of five design principles in object-oriented programming aimed at making software more maintainable, scalable, and robust.

---

## 1. **S – Single Responsibility Principle (SRP)**
**Definition:** A class should have only **one reason to change**, meaning it should only perform a single responsibility.  

**Example:**
```python
# ❌ Violates SRP: Handles both user data and file saving
class User:
    def __init__(self, name):
        self.name = name

    def save_to_file(self):
        # File saving logic
        pass

# ✅ Follows SRP: Separate data handling and file saving
class User:
    def __init__(self, name):
        self.name = name

class UserFileManager:
    def save_to_file(self, user):
        pass
```

---

## 2. **O – Open/Closed Principle (OCP)**
**Definition:** Software entities should be **open for extension but closed for modification**.  
You should be able to add new functionality without changing existing code.

**Example:**
```python
# ❌ Violates OCP: Adding new shapes requires modifying existing code
class AreaCalculator:
    def area(self, shape):
        if shape.type == "circle":
            return 3.14 * shape.radius ** 2
        elif shape.type == "square":
            return shape.side ** 2

# ✅ Follows OCP: Extend by adding new classes
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
```

---

## 3. **L – Liskov Substitution Principle (LSP)**
**Definition:** Subclasses should be replaceable with their base classes without altering the correctness of the program.

**Example:**
```python
# ❌ Violates LSP
class Bird:
    def fly(self):
        pass

class Ostrich(Bird):  # Ostrich can't fly
    def fly(self):
        raise Exception("Can't fly")

# ✅ Follows LSP
class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Ostrich(Bird):
    pass
```

---

## 4. **I – Interface Segregation Principle (ISP)**
**Definition:** Clients should not be forced to depend on methods they do not use.

**Example:**
```python
# ❌ Violates ISP
class Machine:
    def print(self):
        pass
    def scan(self):
        pass
    def fax(self):
        pass

# ✅ Follows ISP
class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass
```

---

## 5. **D – Dependency Inversion Principle (DIP)**
**Definition:** High-level modules should not depend on low-level modules; both should depend on abstractions.

**Example:**
```python
# ❌ Violates DIP: High-level depends on low-level
class MySQLDatabase:
    def connect(self):
        pass

class DataProcessor:
    def __init__(self):
        self.db = MySQLDatabase()

# ✅ Follows DIP: Depends on abstraction
class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        pass

class DataProcessor:
    def __init__(self, database: Database):
        self.db = database
```

---

## 📌 Summary
| Principle | Goal |
|-----------|------|
| SRP       | One responsibility per class |
| OCP       | Extend without modifying existing code |
| LSP       | Subclasses must behave like their parent class |
| ISP       | Avoid forcing classes to implement unused methods |
| DIP       | Depend on abstractions, not implementations |

**Following SOLID principles leads to cleaner, scalable, and maintainable code.**
