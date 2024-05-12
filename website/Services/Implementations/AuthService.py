from abc import ABC

from website.Repository.Implementations.AuthRepository import AuthRepository
from website.Services.Interfaces.AuthServiceInterface import AuthServiceInterface


class AuthService(AuthServiceInterface, ABC):
    def __init__(self):
        self.auth_repository = AuthRepository()

    def Register(self, validated_data):
        return self.auth_repository.Register(validated_data)
