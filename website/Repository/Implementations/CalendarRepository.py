from abc import ABC

from django.shortcuts import get_object_or_404

from website.Models import Calendar
from website.Repository.Interfaces.CalendarInterface import CalendarInterface

from website.Models.AdviseModel import Advise


class CalendarRepository(CalendarInterface, ABC):
    def store(self, request):
        user_id = request.user.id
        advise = Advise.objects.get(user_id=user_id)
        if advise:
            return Calendar.objects.create(advise_id=advise.id, availability=request.data.get('availability'))
        pass

    def update(self, request, pk):
        user_id = request.user.id
        advise = Advise.objects.get(user_id=user_id)
        calendar = Calendar.objects.get(id=pk)
        if advise:
            for key, value in request.data.items():
                setattr(calendar, key, value)
            calendar.save()
            return calendar
        pass

    def index(self, request):
        user_id = request.user.id
        advise = Advise.objects.get(user_id=user_id)
        if advise:
            return Calendar.objects.get(advise_id=advise.id)

    def destroy(self, request, pk):
        user_id = request.user.id
        advise = Advise.objects.get(user_id=user_id)

        if advise:
            calendar = get_object_or_404(Calendar, id=pk)
            return calendar.delete()
        pass
