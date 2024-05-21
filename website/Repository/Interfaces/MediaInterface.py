from abc import ABC, abstractmethod


class MediaInterface(ABC):
    @abstractmethod
    def store(self, file, event):
        pass
