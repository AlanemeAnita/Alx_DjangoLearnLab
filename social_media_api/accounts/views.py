from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import RegisterSerializer, UserSerializer
from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Follow / Unfollow actions
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    target = get_object_or_404(User, pk=user_id)
    request.user.following.add(target)
    return Response({'detail': f'Now following {target.username}'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    target = get_object_or_404(User, pk=user_id)
    request.user.following.remove(target)
    return Response({'detail': f'Unfollowed {target.username}'}, status=status.HTTP_200_OK)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': token.user.username
        })

# accounts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowUserView(APIView):
    def post(self, request, pk):
        try:
            user_to_follow = User.objects.get(pk=pk)
            request.user.following.add(user_to_follow)
            return Response({"detail": "User followed successfully."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class UnfollowUserView(APIView):
    def post(self, request, pk):
        try:
            user_to_unfollow = User.objects.get(pk=pk)
            request.user.following.remove(user_to_unfollow)
            return Response({"detail": "User unfollowed successfully."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

