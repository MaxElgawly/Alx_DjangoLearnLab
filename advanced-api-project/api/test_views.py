# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints including CRUD,
    filtering, searching, ordering, and permission checks.
    """

    def setUp(self):
        # Create a user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create an author and some books
        self.author = Author.objects.create(name='George Orwell')
        self.book1 = Book.objects.create(
            title='1984', publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(
            title='Animal Farm', publication_year=1945, author=self.author)

        # Endpoints
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')

    # ------------------------
    # Test List and Detail
    # ------------------------
    def test_list_books(self):
        """Ensure we can list all books (no auth required)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """Ensure we can retrieve a single book by id."""
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    # ------------------------
    # Test Create (requires auth)
    # ------------------------
    def test_create_book_requires_auth(self):
        """Unauthenticated user should get 403 Forbidden."""
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Authenticated user can create a book."""
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    # ------------------------
    # Test Update (requires auth)
    # ------------------------
    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-update', args=[self.book1.id])
        data = {
            'title': '1984 Updated',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, '1984 Updated')

    # ------------------------
    # Test Delete (requires auth)
    # ------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('book-delete', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ------------------------
    # Test Filtering, Searching, Ordering
    # ------------------------
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=1984')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_search_books_by_keyword(self):
        response = self.client.get(self.list_url + '?search=Animal')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Animal Farm')

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.list_url + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # first item should be newer publication year (1949 > 1945)
        self.assertEqual(response.data[0]['title'], '1984')
