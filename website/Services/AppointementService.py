from website.Repository.Implementations.AppointementRepository import AppointementRepository


class AppointementService:
    def __init__(self):
        self.AppointementRepository = AppointementRepository()

    def store_appointement(self, id, request):
        return self.AppointementRepository.store(id, request)

    def index_appointement(self, request):
        return self.AppointementRepository.index(request)

    def show(self, request):
        return self.AppointementRepository.show(request)

    def stats(self, id):
        return self.AppointementRepository.stats(id)