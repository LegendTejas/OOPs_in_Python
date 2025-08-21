# Updated content for library.py

def search_by_author(self, author_name):
    """
    Search for books by a specific author.
    """
    return [book for book in self.books if book.author == author_name]