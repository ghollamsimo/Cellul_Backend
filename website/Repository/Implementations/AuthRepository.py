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
import uuid
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class AuthRepository(AuthInterface, ABC):

    def Register(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        hashed_password = make_password(password)

        email = validated_data.get('email')
        #if role == 'Student' and not email.endswith('@edu.uca.ma'):
        #   raise serializers.ValidationError({'email': 'Please use your academic email ended by (@edu.uca.ma)'})

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

    def Login(self, email):
        user = User.objects.get(email=email)
        return user
        pass

    def Logout(self, user):
        return User.objects.get(user)
        pass

    def get_user(self, id):
        user = User.objects.get(id=id)
        return user

    def forgot_password(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            token = str(uuid.uuid4())
            user.reset_password_token = token
            user.reset_password_sent_at = timezone.now()
            user.save()

            reset_url = request.build_absolute_uri(
                reverse('reset-password', kwargs={'token': token})
            )
            return send_mail(
                'Password Reset Request',
                f'Please click the link to reset your password: {reset_url}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
        except User.DoesNotExist:
            return ['just for testing']
