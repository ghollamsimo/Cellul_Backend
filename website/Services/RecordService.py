from website.Repository.Implementations.RecordRepository import RecordRepository


class RecordService:
    def __init__(self):
        self.RecordRepository = RecordRepository()

    def store(self, request, id):
        return self.RecordRepository.store(request, id)

    def update(self, request, pk):
        return self.RecordRepository.update(request, pk)

    def delete(self, request, pk):
        return self.RecordRepository.destroy(request, pk)

    def index(self, request):
        return self.RecordRepository.index(request)