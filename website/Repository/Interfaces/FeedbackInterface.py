from abc import ABC, abstractmethod


class FeedbackInterface(ABC):
    @abstractmethod
    def store(self, request, advise):
        pass

    def index(self, request):
        pass

    def update(self, pk, request):
        pass

    def destroy(self, pk, student):
        pass