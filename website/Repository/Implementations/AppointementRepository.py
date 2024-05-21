from abc import ABC

from django.shortcuts import get_object_or_404

from website.Models.StudentModel import Student
from website.Models.UserModel import User
from website.Models.AppointementModel import Appointment
from website.Models.AdviseModel import Advise
from website.Repository.Interfaces.AppointementInterface import AppointementInterface


class AppointementRepository(AppointementInterface, ABC):
    def store(self, id):
        global student
        users = User.objects.all()
        for user in users:
            student = Student.objects.get(user=user.id)
        advise = get_object_or_404(Advise, user__id=id)
        date = None
        time = None
        appointement = Appointment.objects.create(
            advise=advise,
            student=student.id,
            date=date,
            time=time
        )
        return appointement
        pass
