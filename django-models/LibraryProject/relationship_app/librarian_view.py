from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .utils.role_checker import is_librarian



@user_passes_test(lambda user: hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian')
def librarianview(request):
    return render(request, 'relationship_app/librarian_view.html')