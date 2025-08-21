# library.py
from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    title: str
    author: str
    is_available: bool = True

    def borrow(self) -> None:
        self.is_available = False

    def return_book(self) -> None:
        self.is_available = True

    def __str__(self) -> str:
        return f"{self.title} by {self.author}" + (" [Available]" if self.is_available else " [Borrowed]")


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, title: str, author: str) -> None:
        self.books.append(Book(title=title, author=author))

    def borrow_book(self, title: str) -> bool:
        q = title.strip().lower()
        for b in self.books:
            if b.title.lower() == q and b.is_available:
                b.borrow()
                return True
        return False

    def return_book(self, title: str) -> bool:
        q = title.strip().lower()
        for b in self.books:
            if b.title.lower() == q and not b.is_available:
                b.return_book()
                return True
        return False

    def list_books(self) -> None:
        if not self.books:
            print("📚 The library is empty.")
            return
        for b in self.books:
            print(b)

    def search_by_author(self, author_name):
        """
        Search for books by a specific author (case-insensitive).
        """
        return [
            book for book in self.books
            if book.author.lower() == author_name.lower()
        ]
