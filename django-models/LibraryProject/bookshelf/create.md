from bookshelf.models import Book

# command
Book.objects.create(title='1984', author='George Orwell', publication_year='1949')
book = Book(title='1984', author='George Orwell', publication_year='1949')

# Upon a successful creation you will see this >>>
