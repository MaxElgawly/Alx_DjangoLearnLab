from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Existing BookList view can stay for just listing if needed
# class BookList(...)

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD actions for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

