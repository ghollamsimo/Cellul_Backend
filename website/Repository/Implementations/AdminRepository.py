from abc import ABC

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
