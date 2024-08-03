from django.contrib.auth.hashers import check_password, make_password
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse

from website.Models import User
from website.Serializers.UserSerializer import UserSerializer
from website.Services.AuthService import AuthService
from django.contrib import messages
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


@method_decorator(csrf_exempt, name='dispatch')
class AuthView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, action=None):
        if action == 'register':
            return self.register(request)
        elif action == 'login':
            return self.login(request)
        elif action == 'logout':
            return self.logout(request)
        elif action == 'forgot_password':
            return self.forgot_password(request)
        elif action == 'change_password':
            return self.change_password(request)
        else:
            return Response({'message': 'Action not specified'}, status=400)

    def delete(self, request, id, action=None):
        if action == 'delete_account':
            return self.delete_account(request, id)

    def register(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        role = request.data.get('role')
        password = request.data.get('password')
        if not role or not password or not email or not name:
            return Response({'message': 'Role, name, email, and password are required'}, status=400)

        try:
            auth_service = AuthService()
            user = auth_service.Register({
                'name': name,
                'email': email,
                'role': role,
                'password': password
            })
            auth_service.email_verification(user, email)
            return Response({'message': 'User registered successfully'}, status=201)
        except serializers.ValidationError as e:
            return Response({'message': 'Validation error', 'details': e.detail}, status=400)

    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        auth_service = AuthService()
        return auth_service.Login(email=email, password=password)

    def logout(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'You are not logged in.'}, status=401)

        auth_service = AuthService()
        auth_service.Logout(request.user)
        User.auth_token.delete()

        refresh_token = RefreshToken.for_user(request.user)
        refresh_token.blacklist()

        return JsonResponse({'message': 'Logout successful.'})

    def get(self, request, uidb64, token):
        auth_service = AuthService()
        success, message = auth_service.activate_account(uidb64, token)
        if success:
            return render(request, 'account_activation_page.html', {'message': message})
        else:
            return render(request, 'account_activation_invalid.html', {'message': message})

    def forgot_password(self, request):
        auth_service = AuthService()
        response = auth_service.forgot_password(request)
        return response

    def reset_password(self, request):
        token = request.data.get('token')
        password = request.data.get('password')
        auth_service = AuthService()
        response = auth_service.reset_password(token, password)
        if response:
            return render(request, 'forgot_password_email.html')

    def delete_account(self, request, id):
        if request.method == 'DELETE':
            auth_service = AuthService()
            auth = auth_service.delete_account(id)
            return JsonResponse({'message': 'Account Deleted SuccessFully'}, status=200)

    def change_password(self, request):
        if request.method == 'POST':
            auth_service = AuthService()
            password = auth_service.change_password(request)
            return JsonResponse({'message': 'Password Changed Success'}, status=200)


def show_user(self, id, action=None):
    if action == 'get_user':
        auth_service = AuthService()
        user = auth_service.get_user_id(id)
        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, status=200)
