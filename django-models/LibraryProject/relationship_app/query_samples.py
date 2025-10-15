from relationship_app.models import Author, Book, Library, Librarian

# --- Query 1: All books by a specific author ---
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


# --- Query 2: List all books in a specific library ---
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# --- Query 3: Retrieve the librarian for a specific library ---
def librarian_for_library(library_name):
    library = Librarian.objects.get(name=library_name)
    return library.librarian


# Example usage
if __name__ == "__main__":
    # Populate data for testing
    author1, _ = Author.objects.get_or_create(name="George Orwell")
    book1, _ = Book.objects.get_or_create(title="1984", author=author1)
    book2, _ = Book.objects.get_or_create(title="Animal Farm", author=author1)

    library1, _ = Library.objects.get_or_create(name="Central Library")
    library1.books.set([book1, book2])

    librarian1, _ = Librarian.objects.get_or_create(name="John Doe", library=library1)

    print("Books by George Orwell:", [b.title for b in books_by_author("George Orwell")])
    print("Books in Central Library:", [b.title for b in books_in_library("Central Library")])
    print("Librarian for Central Library:", librarian_for_library("Central Library").name)

