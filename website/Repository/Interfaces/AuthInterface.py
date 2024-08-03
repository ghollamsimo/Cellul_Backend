from abc import ABC, abstractmethod


class AuthInterface(ABC):
    @abstractmethod
    def Register(self, validated_data):
        pass

    def Login(self, email):
        pass

    def Logout(self, user):
        pass

    def get_user(self, id):
        pass

    def forgot_password(self, request):
        pass

    def delete_account(self, id):
        pass

    def change_password(self, request):
        pass