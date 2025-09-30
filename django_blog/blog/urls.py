from django.urls import path
from .views import RegisterView
from . import views
from django.contrib.auth import views as auth_views











urlpatterns = [
    path('', views.home, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('profile/', views.profile, name='profile'),
]