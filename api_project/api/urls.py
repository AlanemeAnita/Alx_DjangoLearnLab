from django.urls import path
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Hello, API is working!"})

urlpatterns = [
    path('', home, name='home'),
]

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
    # Existing endpoint for list only
    path('books/', BookList.as_view(), name='book-list'),

    # All CRUD endpoints via the router
    path('', include(router.urls)),
]
