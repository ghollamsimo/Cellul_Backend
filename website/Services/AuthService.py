from abc import ABC

from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken

from website.Models import User
from website.Repository.Implementations.AuthRepository import AuthRepository
from website.Serializers.UserSerializer import UserSerializer


class AuthService:
    def __init__(self):
        self.AuthRepository = AuthRepository()

    def Register(self, validated_data):
        return self.AuthRepository.Register(validated_data)

    def Login(self, email, password):
        if not email or not password:
            return JsonResponse({'message': 'Email and password required'}, status=400)
        try:
            user = self.AuthRepository.Login(email=email)
            if user and check_password(password, user.password):
                token = RefreshToken.for_user(user)
                user_serializer = UserSerializer(user)
                return JsonResponse({'token': str(token.access_token), 'user': user_serializer.data})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=400)


def Logout(self, user):
        return self.AuthRepository.Logout(user)
