# bookshelf/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .models import Book

def form_example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Safe handling of user input
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            Book.objects.create(title=title, author=author)
            return render(request, 'bookshelf/form_success.html', {'form': form})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("Book created (if this were a real form).")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Book '{book.title}' edited successfully.")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Book '{book.title}' deleted successfully.")


# Security settings explanation:
# SECURE_BROWSER_XSS_FILTER enables browser XSS protection
# X_FRAME_OPTIONS='DENY' prevents clickjacking
# SECURE_CONTENT_TYPE_NOSNIFF stops content type sniffing
# CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE ensure cookies only sent over HTTPS

