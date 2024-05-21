from abc import ABC, abstractmethod


class AppointementInterface(ABC):
    @abstractmethod
    def store(self, id):
        pass