from django.urls import path
from .views import VideoListCreateAPIView, CommentListCreateAPIView,LikeAPIView, SubscriptionAPIView,LikeCountAPIView,VideoDetailAPIView,LoginAPIView,RegisterAPIView,increment_video_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('videos/', VideoListCreateAPIView.as_view(), name='video-list-create'),
    path('videos/<int:video_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('videos/<int:video_id>/like/', LikeAPIView.as_view(), name='video-like'),
    path('users/<int:creator_id>/subscribe/', SubscriptionAPIView.as_view(), name='user-subscribe'),
    path('videos/<int:video_id>/likecount', LikeCountAPIView.as_view(), name='LikeCountAPIView'),
    path('videos/<int:video_id>/videos', VideoDetailAPIView.as_view(), name='VideoDetailAPIView'),
    path('register/',RegisterAPIView.as_view(), name='RegisterAPIView'),
    path('login/', LoginAPIView.as_view(), name='LoginAPIView'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

