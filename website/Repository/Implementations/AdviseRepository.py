from abc import ABC

from django.shortcuts import get_object_or_404
from flask.sansio.app import App

from website.Models.AdviseModel import Advise
from website.Models.NotificationModel import Notification
from website.Models.AppointementModel import Appointment
from website.Repository.Interfaces.AdviseInterface import AdviseInterface


class AdviseRepository(AdviseInterface, ABC):
    def handle_appointment(self, pk, status):
        appointement = get_object_or_404(Appointment, pk=pk)
        student_id = appointement.student_id

        if status == 'Accepted':
            appointement.status = 'Accepted'
            message = 'Your Appointment Has Been Accepted'
        elif status == 'Rejected':
            appointement.status = 'Rejected'
            message = 'Your Appointment Has Been Rejected'
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