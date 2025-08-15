from abc import ABC, abstractmethod

# --------------------------
# Abstract Class: Notification
# --------------------------
class Notification(ABC):
    @abstractmethod
    def notify(self, message):
        pass

# --------------------------
# Book Class
# --------------------------
class Book:
    _book_counter = 1000  # Class variable to assign unique IDs

    def __init__(self, title, author):
        self.__book_id = Book._book_counter  # Private attribute
        Book._book_counter += 1
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.__book_id}] '{self.title}' by {self.author} - {status}"

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

    # Magic method for equality (used in lists)
    def __eq__(self, other):
        return self.__book_id == other.__book_id

# --------------------------
# Member Class
# --------------------------
class Member(Notification):
    total_members = 0  # Class variable

    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance      # Private attribute
        self.borrowed_books = []      # Instance attribute
        Member.total_members += 1

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            self.notify(f"{self.name} borrowed '{book.title}'")
        else:
            self.notify(f"'{book.title}' is already borrowed")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            self.notify(f"{self.name} returned '{book.title}'")

    def notify(self, message):  # Implementation of abstract method
        print(f"[Notification] {message}")

    def show_balance(self):
        print(f"{self.name}'s Balance: ${self.__balance}")

    # Property decorator for encapsulated balance
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

    def __str__(self):
        return f"Member: {self.name}, Borrowed Books: {len(self.borrowed_books)}"

# --------------------------
# PremiumMember Class (Inheritance & Polymorphism)
# --------------------------
class PremiumMember(Member):
    def borrow_book(self, book):
        # Premium members can borrow even if limit exceeded
        if book.borrow():
            self.borrowed_books.append(book)
            self.notify(f"Premium member {self.name} borrowed '{book.title}'")
        else:
            self.notify(f"'{book.title}' is already borrowed")

# --------------------------
# Library Class
# --------------------------
class Library:
    def __init__(self):
        self.books = []

    # Instance method
    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    # Static method
    @staticmethod
    def library_rules():
        print("Library Rules: \n1. Return books on time\n2. Handle books carefully")

    # Magic methods
    def __len__(self):
        return len(self.books)

    def __getitem__(self, index):
        return self.books[index]

# --------------------------
# Demo / Usage
# --------------------------
# Create library
lib = Library()

# Add books
lib.add_book(Book("Python Mastery", "Alice"))
lib.add_book(Book("Data Science Handbook", "Bob"))
lib.add_book(Book("Machine Learning 101", "Charlie"))

# Show library rules
Library.library_rules()

# Create members
m1 = Member("John", 50)
m2 = PremiumMember("Emma", 100)

# Borrow books
m1.borrow_book(lib[0])
m1.borrow_book(lib[0])  # Already borrowed
m2.borrow_book(lib[1])

# Show balances and borrowed books
m1.show_balance()
print(m1)
print(m2)

# Return books
m1.return_book(lib[0])

# Check library book count using __len__
print(f"Total books in library: {len(lib)}")
