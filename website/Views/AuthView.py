from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken

from website.Models import User
from website.Serializers.UserSerializer import UserSerializer
from website.Services.AuthService import AuthService

from django.conf import settings
from django.core.mail import send_mail


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


def otp():
    subject = 'Welcome to My Site'
    message = 'Thank you for logging in!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [['email']]

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)
    except Exception as e:
        return JsonResponse({'message': 'Failed to send email: {}'.format(str(e))}, status=500)


@api_view(['POST'])
@csrf_exempt
def post(request):
    if request.method == 'POST':
        auth_service = AuthService()
        return auth_service.Login(request=request)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'}, status=405)


@api_view(['POST'])
def UserLogout(request, user):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return JsonResponse({'message': 'You are not logged in.'}, status=401)

        auth_service = AuthService()
        auth_service.Logout(user)
        User.auth_token.delete()

        refresh_token = RefreshToken.for_user(user)
        refresh_token.blacklist()

        return JsonResponse({'message': 'Logout successful.'})
