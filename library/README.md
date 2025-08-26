# Mini Library

A tiny, in-memory library system with `Book` and `Library` classes. Supports adding, borrowing, returning, and listing books.

## Features
- Add books (title + author)
- Borrow/return by title (case-insensitive)
- Search books by author (exact match)
- Search books by title (partial match)
- Get library statistics (total, available, borrowed counts)
- Verbose borrow operations with detailed error messages
- List all books with availability
- Sort books by title or author
- Export/import to/from JSON
- Zero dependencies (uses Python stdlib)

## Requirements
- Python 3.9+

## Getting Started

### Running the Example Data Seeder

To populate the library with example books for testing and demonstration:

```bash
python seed.py
```

This will create a library with 8 famous books and display them.

### Basic Usage

```bash
python library.py
```

### Expected Output (example):
```
1984 by George Orwell [Available]
The Hobbit by J.R.R. Tolkien [Available]

Borrowing '1984'...
1984 by George Orwell [Borrowed]
The Hobbit by J.R.R. Tolkien [Available]

```

## Library API (quick glance)

```python
from library import Library

lib = Library()
lib.add_book("Dune", "Frank Herbert")
lib.borrow_book("Dune")     # (True, index) if available, (False, None) if not
lib.return_book("Dune")     # True if it was borrowed
lib.list_books()            # prints status

# New features
lib.search_by_title("Du")   # partial match: [Book("Dune", "Frank Herbert")]
lib.stats()                 # {"total": 1, "available": 1, "borrowed": 0}
success, msg = lib.borrow_book_verbose("Dune")  # (True, "Successfully borrowed 'Dune'")
```


NOTE:

Borrow API change:
- `borrow_book(title)` now returns `(bool, Optional[int])`:

    - `(True, index)` when a copy was successfully borrowed (index is the list index of that copy).

    - `(False, None)` if no available copy found.

This enables disambiguation when multiple identical titles exist.
