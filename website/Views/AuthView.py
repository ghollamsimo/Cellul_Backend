from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from website.Services.AuthService import AuthService


@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
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
            return Response({'message': 'User registered successfully'}, status=201)
        except serializers.ValidationError as e:
            return Response({'message': 'Validation error', 'details': e.detail}, status=400)

    else:
        return Response({'message': 'This Function Is Supported Method Post'})


@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'message': 'Email and password required'}, status=400)

        try:
            auth_service = AuthService()
            user = auth_service.Login({'email': email, 'password': password}, request)
            if user:
                return JsonResponse({'message': 'Login successful'})
            else:
                return JsonResponse({'message': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    else:
        return Response({'message': 'Method not allowed'}, status=405)


def UserLogout(request):
    if request.method == 'POST':
        user = None
        if user:
            return JsonResponse({'message': 'Your Not logged'})

        auth_service = AuthService()
        logout = auth_service.Logout(request)
        if logout:
            return JsonResponse({'message': 'You have been logged out'})
        else:
            return JsonResponse({'message': 'error'})