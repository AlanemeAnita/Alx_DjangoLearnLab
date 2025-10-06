from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, UserDetailView, follow_user, unfollow_user, CustomAuthToken, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
]

