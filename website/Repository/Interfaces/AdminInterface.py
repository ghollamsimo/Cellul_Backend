from abc import ABC, abstractmethod


class AdminInterface(ABC):
    @abstractmethod
    def stats(self):
        pass

    @abstractmethod
    def update_user(self, request, id):
        pass

    @abstractmethod
    def destroy(self, request, id):
        pass

    def add_adviser(self, request):
        pass
