 First go to the models.py file iin the app and add the code below the Book model

# command
def __str__(self):
        return f'{self.title}, by {self.author}, in {self.publication_year}'
Book.objects.get()

# upon successful retreival, it would show as;

<QuerySet [<Book: 1984, by George Orwell, in 1949>]>
