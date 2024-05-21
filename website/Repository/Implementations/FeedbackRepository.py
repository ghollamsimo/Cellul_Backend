from abc import ABC

from django.shortcuts import get_object_or_404

from website.Models.AdviseModel import Advise
from website.Models.FeedbackModel import Feedback
from website.Models.StudentModel import Student
from website.Repository.Interfaces.FeedbackInterface import FeedbackInterface


class FeedbackRepository(FeedbackInterface, ABC):
    def store(self, request, advise):
        user_id = request.data.get('user_id')
        feedback = request.data.get('feedback')
        student = Student.objects.get(user_id=user_id)

        if student:
            return Feedback.objects.create(
                student_id=student.id,
                advise_id=advise,
                feedback=feedback
            )

        pass

    def index(self, request):
        user_id = request.data.get('user_id')
        advise = Advise.objects.get(user_id=user_id)
        print('advise', advise)
        feedback = Feedback.objects.filter(advise_id=advise)
        return feedback
        pass

    def update(self, pk, request):
        feedback = Feedback.objects.get(pk=pk)
        for key, value in request.items():
            setattr(feedback, key, value)
        feedback.save()
        return feedback
        pass

    def destroy(self, pk, student):
        student_id = get_object_or_404(Student.id)
        feedback = Feedback.objects.get(pk=pk, student=student_id)
        return feedback.delete()
        pass