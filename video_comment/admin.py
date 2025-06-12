from django.contrib import admin

# Register your models here.
from .models import (User,Video,Comment,Like,Subscription)

admin.site.register(User)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Subscription)