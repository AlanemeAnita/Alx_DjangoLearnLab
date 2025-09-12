# relationship_app/models.py
from django.db import models
from django.conf import settings  # use settings.AUTH_USER_MODEL

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

    def __str__(self):
        return f'{self.title}, {self.author}'

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f'{self.name}'

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class UserProfile(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        LIBRARIAN = 'librarian', 'librarian'
        MEMBER = 'Member', 'Member'

    # Use settings.AUTH_USER_MODEL so it points to your custom user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # CharField needs max_length — set to 20 and give a default
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)

    def __str__(self):
        # friendlier display
        return f'{self.user} ({self.role})'
