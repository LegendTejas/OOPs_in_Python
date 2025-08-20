from dataclasses import dataclass

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
        status = " [Available]" if self.is_available else " [Borrowed]"
        return f"{self.title} by {self.author}{status}"


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, title: str, author: str) -> None:
        self.books.append(Book(title=title, author=author))

    def borrow_book(self, title: str) -> bool:
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower and book.is_available:
                book.borrow()
                return True
        return False

    def return_book(self, title: str) -> bool:
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower and not book.is_available:
                book.return_book()
                return True
        return False

    def list_books(self) -> None:
        if not self.books:
            print("📚 The library is empty.")
            return
        for book in self.books:
            print(book)


if __name__ == "__main__":
    lib = Library()
    lib.add_book("1984", "George Orwell")
    lib.add_book("The Hobbit", "J.R.R. Tolkien")

    lib.list_books()

    print("\nBorrowing '1984'...")
    lib.borrow_book("1984")
    lib.list_books()
