from django.contrib.auth.hashers import check_password
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
        else:
            return Response({'message': 'Action not specified'}, status=400)

    def register(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        role = request.data.get('role')
        password = request.data.get('password')
        if not role or not password or not email or not name:
            return Response({'message': 'Role, name, email, and password are required'}, status=400)

        try:
            auth_service = AuthService()
            auth_service.Register({
                'name': name,
                'email': email,
                'role': role,
                'password': password
            })
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
