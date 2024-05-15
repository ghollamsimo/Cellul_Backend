from abc import ABC, abstractmethod


class NotificationInterface(ABC):
    @abstractmethod
    def store(self):
        pass