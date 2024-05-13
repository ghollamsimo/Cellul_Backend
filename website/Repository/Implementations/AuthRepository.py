from abc import ABC

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import serializers, status

from website.Models.AdminModel import Admin
from website.Models.AdviseModel import Advise
from website.Models.StudentModel import Student
from website.Models.UserModel import User
from website.Repository.Interfaces.AuthInterface import AuthInterface
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class AuthRepository(AuthInterface, ABC):

    def Register(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        hashed_password = make_password(password)

        email = validated_data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})

        user = User.objects.create(password=hashed_password, **validated_data)

        if role == 'Admin':
            admin = Admin.objects.create(user=user)
            return admin
        elif role == 'Student':
            student = Student.objects.create(user=user)
            return student
        elif role == 'Advise':
            advise = Advise.objects.create(user=user)
            return advise
        else:
            raise serializers.ValidationError({'message': 'Invalid role'})
        pass

    def Login(self, validated_data, request):
        if request.method == 'POST':
            email = request.data.get('email')
            password = request.data.get('password')

            if not email or not password:
                return JsonResponse({'error': 'Please provide both email and password'}, status=400)

            user = authenticate(request, email=email, password=password)
            print('User')
            if user is not None:
                token = RefreshToken.for_user(user)
                return JsonResponse({'token': str(token.access_token)})
            else:
                return JsonResponse({'error': 'Invalid email or password'}, status=401)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)

    def Logout(self, request):
        if request.method == 'POST':
            user = request.user
            try:
                token = RefreshToken.for_user(user)
                token.blacklist()
                return JsonResponse({'message': 'Logged out'}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Method not allowed'}, status=405)