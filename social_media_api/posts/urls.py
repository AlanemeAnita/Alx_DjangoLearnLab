from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path, include
from . import views
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', views.FeedView.as_view(), name='feed'),
    path("like/<int:post_id>/", views.LikePostView.as_view(), name="like-post"),
    path("unlike/<int:post_id>/", views.UnlikePostView.as_view(), name="unlike-post"),
    path('posts/<int:pk>/like/', views.LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike_post'),
    path('', include(router.urls)),
]

urlpatterns += router.urls


