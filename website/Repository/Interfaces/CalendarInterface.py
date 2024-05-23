from abc import ABC, abstractmethod


class CalendarInterface(ABC):
    @abstractmethod
    def store(self, request):
        pass

    def update(self, request, pk):
        pass

    def index(self, request):
        pass

    def destroy(self, request, pk):
        pass