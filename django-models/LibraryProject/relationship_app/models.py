from django.db import models
from django.contrib.auth.models import User


# Create your models here.

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
        return f'{self.name}, {self.books}'

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.library}'
    

class UserProfile(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'Admin', 'Admin'
        LIBRARIAN = 'librarian', 'librarian'
        MEMBER = 'Member', 'Member'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        choices=Role.choices
        # default=Role.MEMBER
    )

    def __str__(self):
        return f'{self.user}, {self.role}'




