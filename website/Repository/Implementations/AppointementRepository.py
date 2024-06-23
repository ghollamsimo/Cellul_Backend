from abc import ABC

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from website.Models.StudentModel import Student
from website.Models.UserModel import User
from website.Models.AppointementModel import Appointment
from website.Models.AdviseModel import Advise
from website.Repository.Interfaces.AppointementInterface import AppointementInterface


class AppointementRepository(AppointementInterface, ABC):
    def store(self, id, request):
        user_id = request.user.id
        student = get_object_or_404(Student, user=user_id)
        advise = get_object_or_404(Advise, id=id)

        date = request.data.get('date')
        time = request.data.get('time')

        if not date or not time:
            raise ValueError('Date and time must be provided.')

        appointment = Appointment.objects.create(
            advise=advise,
            student=student,
            date=date,
            time=time
        )

        return appointment
        pass

    def index(self, request):
        user_id = request.user.id
        advise = get_object_or_404(Advise, user_id=user_id)

        if advise:
            appointment = Appointment.objects.filter(advise_id=advise)
            return appointment
        else:
            return serializers.ValidationError({'message': 'No Advise Found'})
