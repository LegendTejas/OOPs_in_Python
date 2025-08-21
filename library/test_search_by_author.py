import unittest
from library import Library, Book

class TestLibrarySearchByAuthor(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book("1984", "George Orwell")
        self.lib.add_book("Animal Farm", "George Orwell")
        self.lib.add_book("The Hobbit", "J.R.R. Tolkien")

    def test_search_by_author_exact(self):
        results = self.lib.search_by_author("George Orwell")
        titles = {book.title for book in results}
        self.assertEqual(titles, {"1984", "Animal Farm"})

    def test_search_by_author_case_insensitive(self):
        results = self.lib.search_by_author("george orwell")
        titles = {book.title for book in results}
        self.assertEqual(titles, {"1984", "Animal Farm"})

    def test_search_by_author_not_found(self):
        results = self.lib.search_by_author("Unknown Author")
        self.assertEqual(results, [])

if __name__ == "__main__":
    unittest.main()