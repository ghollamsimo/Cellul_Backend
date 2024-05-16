from abc import ABC, abstractmethod


class NotificationInterface(ABC):
    @abstractmethod
    def store_of_event(self):
        pass