from abc import ABC

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from website.Models.AdviseModel import Advise
from website.Models.FeedbackModel import Feedback
from website.Models.StudentModel import Student
from website.Repository.Interfaces.FeedbackInterface import FeedbackInterface
from django.conf import settings


class FeedbackRepository(FeedbackInterface, ABC):
    def store(self, request, advise):
        user_id = request.user.id
        feedback = request.data.get('feedback')
        student = Student.objects.get(user_id=user_id)

        if student:
            return Feedback.objects.create(
                student_id=student.id,
                advise_id=advise,
                feedback=feedback,
                status='Waiting'
            )

        pass

    def index(self, advise):
        advise = Advise.objects.get(id=advise)
        feedback = Feedback.objects.filter(advise_id=advise.id, status='Accepted')
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

    def handle_status(self, pk, status):
        feedback = get_object_or_404(Feedback, id=pk)
        student_id = feedback.student_id
        student = get_object_or_404(Student, id=student_id)

        if status == 'Accepted':
            feedback.status = 'Accepted'
            send_mail(
                'Confirmation Appointment',
                f'Your Feedback Has Been Accepted And Now Is Public So Go Check Your Application ',
                settings.DEFAULT_FROM_EMAIL,
                [student.user.email],
                fail_silently=False,
            )
        elif status == 'Rejected':
            feedback.status = 'Rejected'
            send_mail(
                'Confirmation Appointment',
                f'Your Feedback has been Rejected. Try again with another positive feedback !',
                settings.DEFAULT_FROM_EMAIL,
                [student.user.email],
                fail_silently=False,
            )

        feedback.save()
        pass