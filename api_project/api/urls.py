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
