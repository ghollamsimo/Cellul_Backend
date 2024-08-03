from abc import ABC

from django.shortcuts import get_object_or_404
from flask.sansio.app import App

from website.Models import Student
from website.Models.AdviseModel import Advise
from website.Models.NotificationModel import Notification
from website.Models.AppointementModel import Appointment
from website.Repository.Interfaces.AdviseInterface import AdviseInterface
import uuid
from django.utils import timezone
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


class AdviseRepository(AdviseInterface, ABC):
    def handle_appointment(self, pk, status):
        appointement = get_object_or_404(Appointment, pk=pk)
        student_id = appointement.student_id
        student = get_object_or_404(Student, id=student_id)
        if status == 'Accepted':
            appointement.status = 'Accepted'
            message = 'Your Appointment Has Been Accepted'
            send_mail(
                'Confirmation Appointment',
                f'Your Appointment Has Been Accepted At : {appointement.time} So Go Check Your Application ',
                settings.DEFAULT_FROM_EMAIL,
                [student.user.email],
                fail_silently=False,
            )
        elif status == 'Rejected':
            appointement.status = 'Rejected'
            message = 'Your Appointment Has Been Rejected'
            send_mail(
                'Confirmation Appointment',
                f'Your Appointment Has Been Rejected At : {appointement.time} From The Adviser Try Again',
                settings.DEFAULT_FROM_EMAIL,
                [student.user.email],
                fail_silently=False,
            )
        else:
            raise ValueError("Invalid action specified")

        appointement.save()

        advise = get_object_or_404(Advise, pk=appointement.advise_id)
        event_id = None
        Notification.objects.create(
            student_id=student_id,
            advise_id=advise.id,
            message=message,
            appointment_id=appointement.id,
            event_id=event_id
        )

        return appointement

    def all_advise(self):
        avisers = Advise.objects.all()
        return avisers

    def show(self, pk):
        adviser = get_object_or_404(Advise, id=pk)
        return adviser

    def count(self):
        adviser = Advise.objects.count()
        return adviser
        pass