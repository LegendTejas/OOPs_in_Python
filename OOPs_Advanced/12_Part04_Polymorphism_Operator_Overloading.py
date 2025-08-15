# Operator Overloading
# Giving new meaning to Python operators for custom classes.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __gt__(self, other):
        return self.pages > other.pages

# Creating objects
book1 = Book(150)
book2 = Book(200)

# Using overloaded '+' operator
total_pages = book1 + book2
print(f"Total Pages: {total_pages}")

# Using overloaded '>' operator
print(f"Is book1 bigger? {book1 > book2}")
