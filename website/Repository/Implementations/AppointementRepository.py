from abc import ABC

from django.shortcuts import get_object_or_404
from rest_framework import serializers

from website.Models.StudentModel import Student
from website.Models.UserModel import User
from website.Models.AppointementModel import Appointment
from website.Models.AdviseModel import Advise
from website.Repository.Interfaces.AppointementInterface import AppointementInterface

from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


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
        send_mail(
            'New Appointment Created',
            f'{student.user.email} Make New Appointment At: {appointment.time}',
            settings.DEFAULT_FROM_EMAIL,
            [advise.user.email],
            fail_silently=False,
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

    def show(self, request):
        user_id = request.user.id
        student = Student.objects.get(id=user_id)
        appointment = Appointment.objects.get(student_id=student.id, status='Accepted')
        return appointment

    def stats(self, id):
        advise = Advise.objects.get(id=id)
        appointment = Appointment.objects.filter(advise_id=advise, status='Accepted').count()
        return appointment
