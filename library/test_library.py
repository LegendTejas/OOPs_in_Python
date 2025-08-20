import pytest
from library.library import Library

def test_add_and_list_books(capsys):
    lib = Library()
    lib.add_book("1984", "George Orwell")
    lib.add_book("The Hobbit", "J.R.R. Tolkien")

    lib.list_books()
    captured = capsys.readouterr()
    assert "1984 by George Orwell [Available]" in captured.out
    assert "The Hobbit by J.R.R. Tolkien [Available]" in captured.out

def test_borrow_and_return_book():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")

    assert lib.borrow_book("Dune") is True
    assert lib.borrow_book("Dune") is False   # already borrowed

    assert lib.return_book("Dune") is True
    assert lib.return_book("Dune") is False   # already returned
