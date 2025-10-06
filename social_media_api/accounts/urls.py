from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LoginView, ProfileView, UserDetailView, follow_user, unfollow_user, CustomAuthToken, FollowUserView, UnfollowUserView

urlpatterns = [
    path('/register', RegisterView.as_view(), name='register'),
    path('/login', LoginView.as_view(), name='login'),
    path('/profile', ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow_user'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]