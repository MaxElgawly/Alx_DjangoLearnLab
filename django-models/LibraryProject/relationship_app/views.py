from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Librarian, Library

def list_all_books(request):
    books = Book.objects.all()
    return render(request, 'templates/list_book.html', {'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'templates/library_detail.html'
    context_object_name = 'library'
    
    def get_queryset(self):
        return super().get_queryset()()

