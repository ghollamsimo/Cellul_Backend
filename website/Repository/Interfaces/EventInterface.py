from abc import ABC, abstractmethod


class EventInterface(ABC):
    @abstractmethod
    def store(self, request):
        pass

    @abstractmethod
    def update(self, pk, validated_data, request):
        pass

    @abstractmethod
    def index(self, request):
        pass

    @abstractmethod
    def destroy(self, pk, request):
        pass

