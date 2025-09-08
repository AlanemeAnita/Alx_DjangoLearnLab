## Django Shell CRUD Operation

from bookshelf.models import Book

# CREATE
book = Book(title='1984', author='George Orwell', publication_year='1949')
book.save()

# READ/RETRIEVE
book = Book.objects.all()
book

# UPDATE
book = Book.objects.first()
book.title = 'Nineteen Eighty-Four'
book.save()

# DELETE
book.objects.first()
book.delete()

