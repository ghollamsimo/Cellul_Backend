from abc import ABC, abstractmethod


class AuthInterface(ABC):
    @abstractmethod
    def Register(self, validated_data):
        pass

    def Login(self, email, password):
        pass

    def Logout(self, request):
        pass
