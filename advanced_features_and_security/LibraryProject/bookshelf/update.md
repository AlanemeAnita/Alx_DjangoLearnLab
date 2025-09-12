from bookshelf.models import Book

# command
book = Book.objects.first()
book.title = Nineteen Eighty-Four
book.save()

# upon successfull update, the output would be;

<Book: Nineteen Eighty-Four, by George Orwell, in 1949>
