from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# --- Function-Based View ---
def list_books(request):
    """Display all books and their authors."""
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

# --- Class-Based View ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

