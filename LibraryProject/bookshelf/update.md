from library\_bookshelf.models import Book



\# Update a Book

book = Book.objects.get(title="1984")

book.title = "Nineteen Eighty-Four"

book.save()



\# Verify update

Book.objects.get(id=book.id).title

\# Expected output: 'Nineteen Eighty-Four'



