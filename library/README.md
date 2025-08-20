# Mini Library

A tiny, in-memory library system with `Book` and `Library` classes. Supports adding, borrowing, returning, and listing books.

## Features
- Add books (title + author)
- Borrow/return by title (case-insensitive)
- List all books with availability
- Zero dependencies (uses Python stdlib)

## Requirements
- Python 3.9+

## Getting Started
`library.py`

### Expected Output (example):
```
1984 by George Orwell [Available]
The Hobbit by J.R.R. Tolkien [Available]

Borrowing '1984'...
1984 by George Orwell [Borrowed]
The Hobbit by J.R.R. Tolkien [Available]

```

## Library API (quick glance)

```
from library import Library

lib = Library()
lib.add_book("Dune", "Frank Herbert")
lib.borrow_book("Dune")     # True if available
lib.return_book("Dune")     # True if it was borrowed
lib.list_books()            # prints status
```
