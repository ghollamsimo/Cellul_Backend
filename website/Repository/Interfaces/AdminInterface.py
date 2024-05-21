from abc import ABC, abstractmethod


class AdminInterface(ABC):
    @abstractmethod
    def stats(self):
        pass