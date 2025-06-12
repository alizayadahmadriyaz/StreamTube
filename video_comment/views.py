from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (User,Video,Comment,Like,Subscription)
from .serializers import UserSerializer,VideoSerializer,CommentSerializer,LikeSerializer,SubscriptionSerializer,LoginSerializer,RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import F
from rest_framework.decorators import api_view

# Create your views here.
class VideoListCreateAPIView(APIView):
    def get(self, request):
        videos = Video.objects.all().order_by('-created_at')
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentListCreateAPIView(APIView):
    def get(self, request, video_id):
        comments = Comment.objects.filter(video_id=video_id).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, video_id):
        print(request.data)
        serializer = CommentSerializer(data=request.data)
        print(request.user)
        print("ssssssssssssssss")
        print(serializer)
        if serializer.is_valid():
            serializer.save(user=request.user, video_id=video_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("galat")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeAPIView(APIView):
    def post(self, request, video_id):
        video = get_object_or_404(Video, id=video_id)
        is_like = request.data.get("is_like", True)

        like, created = Like.objects.get_or_create(video=video, user=request.user)
        like.is_like = is_like
        like.save()

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)

    def delete(self, request, video_id):
        video = get_object_or_404(Video, id=video_id)
        try:
            like = Like.objects.get(video=video, user=request.user)
            like.delete()
            return Response({"message": "Like removed."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"error": "Like does not exist."}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.permissions import IsAuthenticated    
class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,creator_id):
        print(request.user)
        ans=Subscription.objects.filter(subscriber=request.user, creator_id=creator_id).exists()
        print(ans)
        if(ans==1):
            return Response({'message':1})
        return Response({'message':0})
    def post(self, request, creator_id):
        creator = get_object_or_404(User, id=creator_id)

        if request.user == creator:
            print("my name is khan")
            return Response({"error": "You cannot subscribe to yourself."}, status=status.HTTP_400_BAD_REQUEST)

        subscription, created = Subscription.objects.get_or_create(subscriber=request.user, creator=creator)

        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)

    def delete(self, request, creator_id):
        try:
            subscription = Subscription.objects.get(subscriber=request.user, creator_id=creator_id)
            subscription.delete()
            return Response({"message": "Unsubscribed successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=status.HTTP_404_NOT_FOUND)

class LikeCountAPIView(APIView):
    def get(self, request, video_id):
        video = get_object_or_404(Video, id=video_id)

        like_count = Like.objects.filter(video=video, is_like=True).count()
        dislike_count = Like.objects.filter(video=video, is_like=False).count()

        return Response({
            "video_id": video_id,
            "likes": like_count,
            "dislikes": dislike_count,
        }, status=status.HTTP_200_OK)


# Add to views.py
class VideoDetailAPIView(APIView):
    def get(self, request, video_id):
        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({"error": "Video not found"}, status=404)
        serializer = VideoSerializer(video)
        return Response(serializer.data)


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def increment_video_views(request, video_id):
    try:
        # Use F() to avoid race conditions and ensure atomic update
        video = Video.objects.get(id=video_id)
        Video.objects.filter(id=video_id).update(views=F('views') + 1)
        
        # Get updated video
        video.refresh_from_db()
        
        return Response({
            'success': True,
            'views': video.views
        })
        
    except Video.DoesNotExist:
        return Response({'error': 'Video not found'}, status=404)
