from django.db import models
from video_comment.models import *
# Create your models here.

# models.py
class ViewTracker(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='view_tracks')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.CharField(max_length=45)
    session_key = models.CharField(max_length=40)
    viewed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['video', 'user'], 
                condition=models.Q(user__isnull=False),
                name='unique_user_video_view'
            ),
            models.UniqueConstraint(
                fields=['video', 'ip_address', 'session_key'],
                condition=models.Q(user__isnull=True),
                name='unique_anonymous_video_view'
            )
        ]
        indexes = [
            models.Index(fields=['video', 'ip_address']),
            models.Index(fields=['video', 'user']),
        ]
