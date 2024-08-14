
from .models import Book,Librarian,Library,Author

#Query all books by a specific author.
author = Author.objects.get(pk=1)
Book.objects.filter(author = author)

# List all books in a library.
library_instance = Library.objects.get(pk=1)
books = library_instance.books.all()

# Retrieve the librarian for a library.
library_instance = Library.objects.get(pk=4)  
librarian = library_instance.librarian
