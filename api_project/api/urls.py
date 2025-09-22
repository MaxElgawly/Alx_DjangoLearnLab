from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Include all router URLs for the viewset
    path('', include(router.urls)),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # 👈 built-in token view
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing endpoints
    path('books/', BookList.as_view(), name='book-list'),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Router endpoints
    path('', include(router.urls)),
]


