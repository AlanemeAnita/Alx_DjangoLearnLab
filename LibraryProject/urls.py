"""LibraryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information, see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')),  # make sure bookshelf/urls.py exists
]
