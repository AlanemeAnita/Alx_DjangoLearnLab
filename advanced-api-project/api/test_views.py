# api/test_views.py
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Tests for Book API endpoints:
      - list, search, filter, ordering (public)
      - create, update, delete (authenticated)
    """

    def setUp(self):
        # Create a user for auth-required operations
        self.user = User.objects.create_user(username='tester', password='testpass123')

        # Create two authors and two books
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='James Clear')

        self.book1 = Book.objects.create(title='Harry Potter', publication_year=1997, author=self.author1)
        self.book2 = Book.objects.create(title='Atomic Habits', publication_year=2018, author=self.author2)

        # Endpoints (use literal paths that exist in the project)
        self.list_url = '/api/books/'
        self.create_url = '/api/books/create/'

    # -------------------------
    # READ / LIST tests (public)
    # -------------------------
    def test_list_books_public(self):
        """Anyone can GET the list of books (200 OK)."""
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        # Expect at least the two books we added
        titles = [item['title'] for item in resp.json()]
        self.assertIn('Harry Potter', titles)
        self.assertIn('Atomic Habits', titles)

    def test_search_books_by_title_or_author(self):
        """Search param should find books by title or author name."""
        resp1 = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(resp1.status_code, status.HTTP_200_OK)
        data1 = resp1.json()
        self.assertTrue(any(item['title'] == 'Harry Potter' for item in data1))

        resp2 = self.client.get(self.list_url, {'search': 'James'})
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
        data2 = resp2.json()
        self.assertTrue(any(item['title'] == 'Atomic Habits' for item in data2))

    def test_filter_by_publication_year(self):
        """Filtering by publication_year should return expected book(s)."""
        resp = self.client.get(self.list_url, {'publication_year': 1997})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        self.assertTrue(all(item['publication_year'] == 1997 for item in data))

    def test_ordering_works(self):
        """Ordering by -publication_year should return book2 first (2018)."""
        resp = self.client.get(self.list_url, {'ordering': '-publication_year'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = resp.json()
        if len(data) >= 2:
            self.assertEqual(data[0]['title'], 'Atomic Habits')  # 2018 first

    # -------------------------
    # WRITE tests (authenticated)
    # -------------------------
    def test_create_book_requires_authentication(self):
        """POST without auth must be forbidden (403)."""
        payload = {'title': 'New Book', 'publication_year': 2020, 'author': self.author1.id}
        resp = self.client.post(self.create_url, payload, format='json')
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_create_book_authenticated(self):
        """Authenticated user can create a book (201)."""
        self.client.login(username='tester', password='testpass123')  # session auth
        payload = {'title': 'New Book', 'publication_year': 2020, 'author': self.author1.id}
        resp = self.client.post(self.create_url, payload, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        # Confirm book exists
        self.assertTrue(Book.objects.filter(title='New Book').exists())

    def test_update_book_authenticated(self):
        """Authenticated user can update a book (PUT/PATCH)."""
        self.client.login(username='tester', password='testpass123')
        update_url = f'/api/books/{self.book1.id}/update/'
        payload = {'title': 'Harry Potter 1', 'publication_year': self.book1.publication_year, 'author': self.author1.id}
        resp = self.client.put(update_url, payload, format='json')
        self.assertIn(resp.status_code, (status.HTTP_200_OK, status.HTTP_202_ACCEPTED))
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Harry Potter 1')

    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book (DELETE)."""
        self.client.login(username='tester', password='testpass123')
        delete_url = f'/api/books/{self.book2.id}/delete/'
        resp = self.client.delete(delete_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())
