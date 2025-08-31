from library\_bookshelf.models import Book



\# Create a Book instance

book = Book.objects.create(title="1984", author="George Orwell", publication\_year=1949)

book

\# Expected output: <Book: 1984>



