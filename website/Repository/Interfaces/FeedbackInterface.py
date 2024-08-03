from abc import ABC, abstractmethod


class FeedbackInterface(ABC):
    @abstractmethod
    def store(self, request, advise):
        pass

    def index(self, advise):
        pass

    def update(self, pk, request):
        pass

    def destroy(self, pk, student):
        pass

    def handle_status(self, pk, status):
        pass