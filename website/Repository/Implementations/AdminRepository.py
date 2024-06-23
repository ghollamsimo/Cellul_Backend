from abc import ABC

from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password

from website.Models.AdminModel import Admin
from website.Models.EventModel import Event
from website.Models.AppointementModel import Appointment
from website.Models.AdviseModel import Advise
from website.Models.StudentModel import Student
from website.Models.UserModel import User
from website.Repository.Interfaces.AdminInterface import AdminInterface


class AdminRepository(AdminInterface, ABC):
    def stats(self):
        user_count = User.objects.count()
        student_count = Student.objects.count()
        advise_count = Advise.objects.count()
        appointment_count = Appointment.objects.count()
        event_count = Event.objects.count()

        stats_data = {
            'user_count': user_count,
            'student_count': student_count,
            'advise_count': advise_count,
            'appointment_count': appointment_count,
            'event_count': event_count
        }

        return stats_data
        pass

    def update_user(self, request, id):
        user_id = request.user.id
        admin = Admin.objects.get(user=user_id)
        if admin:
            user = get_object_or_404(User, id=id)
            user.email = request.data.get('email')
            user.name = request.data.get('name')
            user.save()
        else:
            return serializers.ValidationError({'message': 'Admin Not Found'})
        pass

    def destroy(self, request, id):
        user_id = request.user.id
        admin = Admin.objects.get(user=user_id)

        if admin:
            user = get_object_or_404(User, id=id)
            return user.delete()
        pass

    def add_adviser(self, request):
        password = request.data.get('password')
        hashed_password = make_password(password)

        user = User.objects.create(
            name=request.data.get('name'),
            email=request.data.get('email'),
            password=hashed_password,
            role='Advise'
        )

        advise = Advise.objects.create(user_id=user.id)
        return advise
        pass