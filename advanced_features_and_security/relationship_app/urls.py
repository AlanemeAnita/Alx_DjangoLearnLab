from django.urls import path
from . import views, admin_view, librarian_view, member_view
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.books, name='books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', admin_view.adminview, name='admin-view'),
    path('librarian/', librarian_view.librarianview, name='librarian-view'),
    path('member/', member_view.memberview, name='member-view'),
    path('add_book/', views.add_book_view, name='add-book'),
    path('edit_book/<int:book_id>/', views.change_book_view, name='change_book'),
    path('delete_book/', views.can_delete_book, name='delete-book')
]
