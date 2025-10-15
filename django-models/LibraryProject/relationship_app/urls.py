from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
    path('login/', LoginView.as_view(template_name="login.html", name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html", name="logout),
    path('register/', views.register_view, name='register'),
]
