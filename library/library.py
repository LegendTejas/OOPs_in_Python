from dataclasses import dataclass

@dataclass
class Book:
    """A class representing a book in the library."""

    title: str
    author: str
    is_available: bool = True

    def borrow(self) -> None:
        """Mark the book as borrowed (set is_available to False)."""
        self.is_available = False

    def return_book(self) -> None:
        """Mark the book as returned (set is_available to True)."""
        self.is_available = True

    def __str__(self) -> str:
        """Return a string representation of the book, with status."""
        status = " [Available]" if self.is_available else " [Borrowed]"
        return f"{self.title} by {self.author}{status}"


class Library:
    """A class to manage a collection of books."""

    def __init__(self) -> None:
        """
        Initialize the library with an empty list of books.
        """
        self.books: list[Book] = []

    def add_book(self, title: str, author: str) -> None:
        """
        Add a new book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.books.append(Book(title=title, author=author))

    def borrow_book(self, title: str) -> bool:
        """
        Borrow a book from the library by its title.

        Args:
            title (str): The title of the book to borrow.

        Returns:
            bool: True if the book was borrowed successfully, False otherwise.
        """
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower and book.is_available:
                book.borrow()
                return True
        return False

    def return_book(self, title: str) -> bool:
        """
        Return a borrowed book to the library by its title.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was returned successfully, False otherwise.
        """
        title_lower = title.lower()
        for book in self.books:
            if book.title.lower() == title_lower and not book.is_available:
                book.return_book()
                return True
        return False

    def list_books(self) -> None:
        """
        Print the list of books in the library.
        """
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