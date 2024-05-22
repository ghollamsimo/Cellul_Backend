from abc import ABC, abstractmethod


class RecordInterface(ABC):
    @abstractmethod
    def store(self, request):
        pass

    def update(self, request, id):
        pass

    def index(self, request):
        pass

    def destroy(self, request, pk):
        pass