import unittest
from library import Library, Book

class TestNewFeatures(unittest.TestCase):
    def setUp(self):
        self.lib = Library()
        self.lib.add_book("The Great Gatsby", "F. Scott Fitzgerald")
        self.lib.add_book("Great Expectations", "Charles Dickens")  
        self.lib.add_book("1984", "George Orwell")
        self.lib.add_book("Animal Farm", "George Orwell")

    def test_search_by_title_partial_match(self):
        """Test partial title search functionality"""
        # Test partial match
        results = self.lib.search_by_title("Great")
        titles = {book.title for book in results}
        self.assertEqual(titles, {"The Great Gatsby", "Great Expectations"})
        
        # Test case insensitive
        results = self.lib.search_by_title("great")
        self.assertEqual(len(results), 2)
        
        # Test single match
        results = self.lib.search_by_title("1984")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "1984")
        
        # Test no match
        results = self.lib.search_by_title("NonExistent")
        self.assertEqual(results, [])

    def test_stats_empty_library(self):
        """Test stats on empty library"""
        empty_lib = Library()
        stats = empty_lib.stats()
        expected = {"total": 0, "available": 0, "borrowed": 0}
        self.assertEqual(stats, expected)

    def test_stats_mixed_library(self):
        """Test stats on library with borrowed and available books"""
        # Initially all available
        stats = self.lib.stats()
        expected = {"total": 4, "available": 4, "borrowed": 0}
        self.assertEqual(stats, expected)
        
        # Borrow two books
        self.lib.borrow_book("1984")
        self.lib.borrow_book("Animal Farm")
        
        stats = self.lib.stats()
        expected = {"total": 4, "available": 2, "borrowed": 2}
        self.assertEqual(stats, expected)

    def test_borrow_book_verbose_success(self):
        """Test verbose borrow with successful borrowing"""
        success, message = self.lib.borrow_book_verbose("1984")
        self.assertTrue(success)
        self.assertIn("Successfully borrowed", message)
        self.assertIn("1984", message)

    def test_borrow_book_verbose_already_borrowed(self):
        """Test verbose borrow when book is already borrowed"""
        # First borrow should succeed
        self.lib.borrow_book("1984")
        
        # Second borrow should fail with specific message
        success, message = self.lib.borrow_book_verbose("1984")
        self.assertFalse(success)
        self.assertIn("already borrowed", message)

    def test_borrow_book_verbose_not_found(self):
        """Test verbose borrow when book is not found"""
        success, message = self.lib.borrow_book_verbose("NonExistent Book")
        self.assertFalse(success)
        self.assertIn("not found", message)

if __name__ == "__main__":
    unittest.main()