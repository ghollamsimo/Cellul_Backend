from abc import ABC, abstractmethod


class AdviseInterface(ABC):
    @abstractmethod
    def handle_appointment(self, pk, status):
        pass

    @abstractmethod
    def all_advise(self):
        pass

    @abstractmethod
    def show(self, pk):
        pass

    @abstractmethod
    def count(self):
        pass