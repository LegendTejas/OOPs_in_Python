# 1. Introduction to Magic/Dunder Methods

# Magic methods are special methods in Python that start and end with double underscores (__method__).
# They let you customize the behavior of objects — for example, how they are printed, compared, added, etc.

# 2 Basic Representation Methods
# __str__ and __repr__ methods

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        # User-friendly string representation
        return f"'{self.title}' with {self.pages} pages"

    def __repr__(self):
        # Developer-friendly representation (debugging)
        return f"Book(title='{self.title}', pages={self.pages})"

# Creating object
book = Book("Python Mastery", 350)

print(str(book))   # Calls __str__
print(repr(book))  # Calls __repr__
