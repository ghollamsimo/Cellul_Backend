from abc import ABC

from django.shortcuts import get_object_or_404

from website.Models.RecordsModel import Record
from website.Models.StudentModel import Student
from website.Models.AdviseModel import Advise
from website.Repository.Interfaces.RecordInterface import RecordInterface


class RecordRepository(RecordInterface, ABC):
    def store(self, request):
        user_id = request.user.id
        advise = Advise.objects.get(user_id=user_id)
        student = get_object_or_404(Student, id=request.data.get('student_id'))
        if advise:
            return Record.objects.create(
                student_id=student.id,
                description=request.data.get('description'),
                advise_id=advise.id
            )
        pass

    def update(self, request, pk):
        user_id = request.user.id
        advise = Advise.objects.get(user_id=user_id)
        record = get_object_or_404(Record, id=pk)
        if advise:
            for key, value in request.items():
                setattr(record, key, value)
            record.save()
        pass

    def index(self, request):
        pass

    def destroy(self, request, pk):
        user_id = request.user.id
        advise = Advise.objects.get(user_id=user_id)

        if advise:
            record = get_object_or_404(Record, id=pk)
            return record.delete()
        pass