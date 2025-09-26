from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
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

class BookListView(generics.ListAPIView):
    """
    GET /books/ – list all books with filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Add filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields you can filter on using ?field=value
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields you can search across using ?search=keyword
    search_fields = ['title', 'author__name']

    # Fields you can order by using ?ordering=title or ?ordering=-publication_year
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering






