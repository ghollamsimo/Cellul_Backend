from abc import ABC, abstractmethod


class AppointementInterface(ABC):
    @abstractmethod
    def store(self, id , request):
        pass

    def index(self, request):
        pass

    def show(self, request):
        pass

    def stats(self, id):
        pass