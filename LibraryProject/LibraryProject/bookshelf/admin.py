from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")  # fields from your Book model
    list_filter = ("author", "publication_year")            # filters for sidebar
    search_fields = ("title", "author")                     # search bar fields
