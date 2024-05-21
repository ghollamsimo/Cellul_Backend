from abc import ABC, abstractmethod


class AuthInterface(ABC):
    @abstractmethod
    def Register(self, validated_data):
        pass

    def Login(self, email):
        pass

    def Logout(self, user):
        pass
