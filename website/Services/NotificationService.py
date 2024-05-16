from website.Repository.Implementations.NotificationRepository import NotificationRepository


class NotificationService:
    def __init__(self):
        self.NotificationRepository = NotificationRepository()

    def store_event_notification(self):
        return self.NotificationRepository.store_of_event()