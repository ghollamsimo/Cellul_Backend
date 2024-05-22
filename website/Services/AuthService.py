from abc import ABC

from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from rest_framework_simplejwt.tokens import AccessToken

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
    
    def email_verification(self,user,email):
            email = email
            token = RefreshToken.for_user(user)
            subject = "Verify your email address"
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': '127.0.0.1:8000',
                'uid':urlsafe_base64_encode(force_bytes(user.id)),
                'token':token,
            })
            email = EmailMessage(
                subject, message, to=[email]
            )
            email.content_subtype = 'html'
            email.send()
    
    def activate_account(self, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            access_token = RefreshToken(token)
            if access_token['user_id'] == int(uid):
                return True, 'Your email has been successfully verified.'
            else:
                return False, 'Invalid token'
        except:
            return False, 'Invalid token'