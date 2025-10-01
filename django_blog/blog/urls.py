from django.urls import path
from .views import RegisterView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views
from django.contrib.auth import views as auth_views











urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path('profile/', views.profile, name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-confirm-delete'),
    # Comment URLs
    path('posts/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='add-comment'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='edit-comment'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete-comment'),

]