from abc import ABC

from website.Repository.Interfaces.NotificationInterface import NotificationInterface


class NotificationRepository(NotificationInterface, ABC):

    def store(self):
        pass