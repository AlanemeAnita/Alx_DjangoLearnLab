from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),  # if you have a urls.py in bookshelf app
]
