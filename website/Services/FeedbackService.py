from website.Repository.Implementations.FeedbackRepository import FeedbackRepository


class FeedbackService:
    def __init__(self):
        self.FeedbackRepository = FeedbackRepository()

    def store_feedback(self, request, advise):
        return self.FeedbackRepository.store(request, advise)

    def index(self, advise):
        return self.FeedbackRepository.index(advise)

    def update_feedback(self, pk, request):
        return self.FeedbackRepository.update(pk, request)

    def destroy_feedback(self, pk, student):
        return self.FeedbackRepository.destroy(pk, student)

    def handle_status(self, pk, status):
        return self.FeedbackRepository.handle_status(pk, status)