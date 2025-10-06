from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .import views
from .views import FeedView, LikePostView, UnlikePostView

urlpatterns = [
    path("feed/", views.FeedView.as_view(), name="feed"),
    path("like/<int:post_id>/", views.LikePostView.as_view(), name="like-post"),
    path("unlike/<int:post_id>/", views.UnlikePostView.as_view(), name="unlike-post"),
]

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls


