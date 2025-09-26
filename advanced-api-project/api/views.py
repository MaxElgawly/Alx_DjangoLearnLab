from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# --------------------------
# List all books (Read-only)
# --------------------------
class BookListView(generics.ListAPIView):
    """
    GET /books/ – list all books.
    Open to all (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view list


# --------------------------
# Retrieve a single book (Read-only)
# --------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<pk>/ – retrieve a single book by ID.
    Open to all (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# --------------------------
# Create a new book
# --------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/ – create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to customize saving behavior.
        Could also log, send signals, etc.
        """
        serializer.save()


# --------------------------
# Update an existing book
# --------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<pk>/update/ – update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook to customize updating behavior.
        """
        serializer.save()


# --------------------------
# Delete an existing book
# --------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<pk>/delete/ – delete an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.


