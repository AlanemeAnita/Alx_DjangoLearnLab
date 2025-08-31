from library\_bookshelf.models import Book



\# Retrieve all books

Book.objects.all()

\# Expected output: <QuerySet \[<Book: 1984>]>



\# Retrieve specific attributes

book = Book.objects.get(title="1984")

book.title  # '1984'

book.author  # 'George Orwell'

book.publication\_year  # 1949



