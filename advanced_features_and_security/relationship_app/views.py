from django.shortcuts import render, redirect, get_object_or_404
from relationship_app.models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from .utils.role_checker import is_admin, is_member, is_librarian
from django.contrib.auth.decorators import permission_required
# Create your views here.





def books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def profile(request):
    return render(request, 'relationship_app/profile.html')

# class register(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'relationship_app/register.html'



@user_passes_test(is_admin)
def adminview(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarianview(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def memberview(request):
    return render(request, 'relationship_app/member_view.html')




@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            Book.objects.create(title=title, author=author)
            return render(request, 'relationship_app/add_success.html')
    return render(request, 'relationship_app/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            book.title = title
            book.author = author
            book.save()
            return redirect('book_detail', book_id=book.id)
    return render(request, 'relationship_app/change_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def can_delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return
    return render(request, 'relationship_app/confirm_delete.html', {'book': book})


