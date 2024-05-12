from abc import ABC, abstractmethod


class AuthInterface(ABC):
    @abstractmethod
    def Register(self, validated_data):
        pass
    @abstractmethod
    def Login(self):
        pass