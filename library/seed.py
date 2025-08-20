from library.library import Library

def seed_library():
    lib = Library()
    lib.add_book("1984", "George Orwell")
    lib.add_book("The Hobbit", "J.R.R. Tolkien")
    lib.add_book("Dune", "Frank Herbert")
    lib.add_book("Pride and Prejudice", "Jane Austen")
    lib.add_book("To Kill a Mockingbird", "Harper Lee")
    lib.add_book("The Catcher in the Rye", "J.D. Salinger")
    lib.add_book("Moby Dick", "Herman Melville")
    lib.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    return lib

if __name__ == "__main__":
    lib = seed_library()
    lib.list_books()
