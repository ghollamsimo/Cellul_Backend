from website.Repository.Implementations.AppointementRepository import AppointementRepository


class AppointementService:
    def __init__(self):
        self.AppointementRepository = AppointementRepository()

    def store_appointement(self, id):
        return self.AppointementRepository.store(id=id)