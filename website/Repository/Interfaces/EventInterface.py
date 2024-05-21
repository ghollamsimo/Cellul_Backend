from abc import ABC, abstractmethod


class EventInterface(ABC):
    @abstractmethod
    def store(self, data, admin):
        pass

    @abstractmethod
    def update(self, pk, validated_data):
        pass

    @abstractmethod
    def index(self, request):
        pass

    @abstractmethod
    def destroy(self, pk):
        pass

