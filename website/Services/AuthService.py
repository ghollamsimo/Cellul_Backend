from abc import ABC

from website.Repository.Implementations.AuthRepository import AuthRepository
from website.Repository.Interfaces.AuthInterface import AuthInterface


class AuthService(AuthInterface, ABC):
    def __init__(self):
        self.AuthRepository = AuthRepository()

    def Register(self, validated_data):
        return self.AuthRepository.Register(validated_data)

    def Login(self, validated_data, request):
        return self.AuthRepository.Login(validated_data, request)

    def Logout(self, request):
        return self.AuthRepository.Logout(request)
