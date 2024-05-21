from abc import ABC, abstractmethod


class NotificationInterface(ABC):
    @abstractmethod
    def store_of_event(self):
        pass

    @abstractmethod
    def store_of_appointment(self):
        pass

    @abstractmethod
    def destroy_of_event(self, request, pk):
        pass

    @abstractmethod
    def destroy_of_appointment(self, request, pk):
        pass