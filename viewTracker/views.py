from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ViewTracker
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import F
from rest_framework.decorators import api_view
from video_comment.models import *
from rest_framework.permissions import IsAuthenticated    


# Create your views here.
# views.py
permission_classes = [IsAuthenticated]
@api_view(['POST'])
def track_video_view_db(request, video_id):

    try:
        print('request user',request.user)
        video = Video.objects.get(id=video_id)
        
        # Get client information
        ip_address = request.META.get('REMOTE_ADDR', '')
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip_address = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
        
        if not request.session.session_key:
            request.session.create()
        session_key = request.session.session_key
        print(ip_address)
        # Check if view already exists
        view_exists = False
        print('authentication ', request.user.is_authenticated)
        if request.user.is_authenticated:
            # For authenticated users, check by user and video
            view_exists = ViewTracker.objects.filter(
                video=video,
                user=request.user
            ).exists()
            print('vire_exit ')
            print(view_exists)
        else:
            # For anonymous users, check by IP + session + video
            view_exists = ViewTracker.objects.filter(
                video=video,
                ip_address=ip_address,
                session_key=session_key,
                user__isnull=True
            ).exists()
        
        if view_exists:
            print({
                'success': False,
                'message': 'View already counted',
                'views': video.views
            })
            return Response({
                'success': False,
                'message': 'View already counted',
                'views': video.views
            })
        
        # Create new view record
        ViewTracker.objects.create(
            video=video,
            user=request.user if request.user.is_authenticated else None,
            ip_address=ip_address,
            session_key=session_key
        )
        
        # Increment view count
        Video.objects.filter(id=video_id).update(views=F('views') + 1)
        video.refresh_from_db()
        
        return Response({
            'success': True,
            'views': video.views,
            'message': 'View counted successfully'
        })
        
    except Exception as e:
        return Response({'error': str(e)}, status=500)
