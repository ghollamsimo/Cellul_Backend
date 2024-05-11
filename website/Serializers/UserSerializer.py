from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import serializers
from website.Models.AdminModel import Admin
from website.Models.AdviseModel import Advise
from website.Models.StudentModel import Student
from website.Models.UserModel import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'role']

    def create(self, validated_data):
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
