from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ("author",)   # filter by author
    search_fields = ("title",)  # search by book title
