from website.Repository.Implementations.AdviseRepository import AdviseRepository


class AdviseService:
    def __init__(self):
        self.AdviseRepository = AdviseRepository()

    def appointment(self, pk, status):
        return self.AdviseRepository.handle_appointment(pk, status)

    def index(self):
        return self.AdviseRepository.all_advise()

    def show(self, pk):
        return self.AdviseRepository.show(pk)

    def count(self):
        return self.AdviseRepository.count()