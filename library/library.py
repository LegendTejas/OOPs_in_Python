# library.py
from dataclasses import dataclass
from typing import List, Optional, Tuple
import json
import os
import argparse
import sys


@dataclass
class Book:
    title: str
    author: str
    is_available: bool = True
    isbn: Optional[str] = None

    def borrow(self) -> None:
        self.is_available = False

    def return_book(self) -> None:
        self.is_available = True

    def __str__(self) -> str:
        isbn_part = f" ISBN:{self.isbn}" if self.isbn else ""
        status = " [Available]" if self.is_available else " [Borrowed]"
        return f"{self.title} by {self.author}{isbn_part}{status}"

    def __repr__(self) -> str:
        return (
            f"Book(title={self.title!r}, author={self.author!r}, "
            f"is_available={self.is_available!r}, isbn={self.isbn!r})"
        )


class Library:
    def __init__(self, allow_duplicates: bool = True) -> None:
        """
        :param allow_duplicates: if False, add_book will raise ValueError on duplicate titles
        """
        self.books: List[Book] = []
        self.allow_duplicates = allow_duplicates

    def add_book(self, title: str, author: str, *, isbn: Optional[str] = None) -> None:
        qtitle = title.strip()
        if not self.allow_duplicates:
            for b in self.books:
                if b.title.strip().lower() == qtitle.lower():
                    raise ValueError(f"Duplicate title not allowed: '{title}'")
        self.books.append(Book(title=qtitle, author=author.strip(), isbn=isbn))

    def borrow_book(self, title: str) -> Tuple[bool, Optional[int]]:
        """
        Borrow the first available copy matching `title` (case-insensitive, stripped).
        Returns (True, index) if borrowed, otherwise (False, None).
        """
        q = title.strip().lower()
        for idx, b in enumerate(self.books):
            if b.title.strip().lower() == q and b.is_available:
                b.borrow()
                return True, idx
        return False, None

    def return_book(self, title: str) -> bool:
        """
        Return the first borrowed copy matching title. Returns True on success.
        """
        q = title.strip().lower()
        for b in self.books:
            if b.title.strip().lower() == q and not b.is_available:
                b.return_book()
                return True
        return False

    def list_books(self) -> List[str]:
        """
        Prints the books (old behavior) and ALSO returns list[str] of printed lines.
        """
        if not self.books:
            print("📚 The library is empty.")
            return []
        lines = [str(b) for b in self.books]
        for line in lines:
            print(line)
        return lines

    def list_books_sorted(self, by: str = "title") -> List[str]:
        """
        Returns & prints a sorted list, stable and case-insensitive.
        by: 'title' or 'author'
        """
        if by not in ("title", "author"):
            raise ValueError("sort key must be 'title' or 'author'")
        sorted_books = sorted(self.books, key=lambda b: getattr(b, by).strip().lower())
        lines = [str(b) for b in sorted_books]
        for line in lines:
            print(line)
        return lines

    def search_by_author(self, author_name: str) -> List[Book]:
        """
        Case-insensitive exact-match search by author.
        """
        q = author_name.strip().lower()
        return [book for book in self.books if book.author.strip().lower() == q]

    def remove_book(self, title: str) -> int:
        """
        Remove ALL books with given title (case-insensitive, trimmed).
        Returns number of removed books.
        """
        q = title.strip().lower()
        before = len(self.books)
        self.books = [b for b in self.books if b.title.strip().lower() != q]
        removed = before - len(self.books)
        return removed

    def to_json(self, path: str) -> None:
        """
        Writes the library to `path` as JSON array:
        [{"title": "...", "author": "...", "is_available": true, "isbn": "..."}]
        """
        payload = [
            {
                "title": b.title,
                "author": b.author,
                "is_available": b.is_available,
                "isbn": b.isbn,
            }
            for b in self.books
        ]
        # ensure dir exists
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)

    def from_json(self, path: str) -> None:
        """
        Loads books from JSON file and appends to current library.
        Handles empty/invalid files gracefully (skips invalid entries).
        """
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Graceful handling: do nothing
            return

        if not isinstance(data, list):
            return

        for item in data:
            if not isinstance(item, dict):
                continue
            title = item.get("title")
            author = item.get("author")
            is_available = item.get("is_available", True)
            isbn = item.get("isbn")
            if not title or not author:
                continue
            # Use add_book but skip duplicates if allow_duplicates is False
            try:
                self.add_book(title, author, isbn=isbn)
            except ValueError:
                # duplicate and duplicates not allowed -> skip
                continue
            # If the JSON indicates borrowed, mark accordingly
            if not is_available:
                # find the last-added book with this title and mark borrowed
                for b in reversed(self.books):
                    if b.title.strip().lower() == title.strip().lower() and b.is_available:
                        b.borrow()
                        break


# Simple CLI
def _build_parser():
    parser = argparse.ArgumentParser(prog="library")
    sub = parser.add_subparsers(dest="cmd", required=True)

    add_p = sub.add_parser("add", help="Add a book")
    add_p.add_argument("--title", required=True)
    add_p.add_argument("--author", required=True)
    add_p.add_argument("--isbn", required=False)

    list_p = sub.add_parser("list", help="List books")
    list_p.add_argument("--sorted-by", choices=["title", "author"], default=None)

    borrow_p = sub.add_parser("borrow", help="Borrow a book (by title)")
    borrow_p.add_argument("--title", required=True)

    return_p = sub.add_parser("return", help="Return a book (by title)")
    return_p.add_argument("--title", required=True)

    remove_p = sub.add_parser("remove", help="Remove all copies of a title")
    remove_p.add_argument("--title", required=True)

    export_p = sub.add_parser("export", help="Export library to JSON")
    export_p.add_argument("--path", required=True)

    import_p = sub.add_parser("import", help="Import library from JSON (append)")
    import_p.add_argument("--path", required=True)

    return parser


def _run_cli():
    parser = _build_parser()
    args = parser.parse_args()

    # For simple CLI usage we instantiate a library in-memory.
    lib = Library()

    if args.cmd == "add":
        lib.add_book(args.title, args.author, isbn=getattr(args, "isbn", None))
        print("Added:", args.title)
    elif args.cmd == "list":
        if args.sorted_by:
            lib.list_books_sorted(by=args.sorted_by)
        else:
            lib.list_books()
    elif args.cmd == "borrow":
        ok, idx = lib.borrow_book(args.title)
        if ok:
            print(f"Borrowed '{args.title}' (index {idx})")
        else:
            print(f"Could not borrow '{args.title}'")
    elif args.cmd == "return":
        ok = lib.return_book(args.title)
        print("Returned." if ok else "Nothing to return.")
    elif args.cmd == "remove":
        removed = lib.remove_book(args.title)
        print(f"Removed {removed} copies.")
    elif args.cmd == "export":
        lib.to_json(args.path)
        print(f"Exported to {args.path}")
    elif args.cmd == "import":
        lib.from_json(args.path)
        print(f"Imported from {args.path}")


if __name__ == "__main__":
    _run_cli()
