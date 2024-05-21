from abc import ABC, abstractmethod


class AdviseInterface(ABC):
    @abstractmethod
    def handle_appointment(self, pk, status):
        pass
