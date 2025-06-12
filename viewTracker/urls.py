from django.urls import path
from .views import *

urlpatterns = [
    path('track/<int:video_id>',track_video_view_db, name='increment_views')
    ]