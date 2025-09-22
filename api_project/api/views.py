from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Include all router URLs for the viewset
    path('', include(router.urls)),
]
