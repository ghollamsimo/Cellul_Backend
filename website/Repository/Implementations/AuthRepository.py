from abc import ABC

from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from rest_framework import serializers, status

from website.Models.AdminModel import Admin
from website.Models.AdviseModel import Advise
from website.Models.StudentModel import Student
from website.Models.UserModel import User
from website.Repository.Interfaces.AuthInterface import AuthInterface
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from website.Serializers.UserSerializer import UserSerializer


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

    def Login(self, email, password, request):
        user = User.objects.get(email=email)
        return user
        pass

    def Logout(self, user):
        return User.objects.get(user)
        pass

