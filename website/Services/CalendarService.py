from website.Repository.Implementations.CalendarRepository import CalendarRepository


class CalendarService:
    def __init__(self):
        self.CalendarRepository = CalendarRepository()

    def store(self, request):
        return self.CalendarRepository.store(request)

    def update(self, request, pk):
        return self.CalendarRepository.update(request, pk)

    def index(self, request):
        return self.CalendarRepository.index(request)

    def destroy(self, request, pk):
        return self.CalendarRepository.destroy(request, pk)