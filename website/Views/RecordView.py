from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from website.Serializers.RecordSerializer import RecordSerializer
from website.Services.RecordService import RecordService


class RecordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, action=None):
        if action == 'all_records':
            return self.all_records(request)

    def post(self, request, action=None):
        if action == 'add_record':
            return self.add_record(request)

    def put(self, request, pk, action=None):
        if action == 'update_record':
            return self.update_record(request, pk)

    def delete(self, request, pk, action=None):
        if action == 'delete_record':
            return self.delete_record(request, pk)

    def add_record(self, request):
        if request.method == 'POST':
            record_service = RecordService()
            record_service.store(request)
            return JsonResponse({'message': 'Record added successfully'})
        pass

    def update_record(self, request, pk):
        if request.method == 'PUT':
            record_service = RecordService()
            record_service.update(request, pk)
            return JsonResponse({'message': 'Record Updated successfully'})
        pass

    def delete_record(self, request, pk):
        if request.method == 'DELETE':
            record_service = RecordService()
            record_service.delete(request, pk)
            return JsonResponse({'message': 'Record Deleted successfully'})
        pass

    def all_records(self, request):
        if request.method == 'GET':
            record_service = RecordService()
            records = record_service.index(request)
            records_serializer = RecordSerializer(records, many=True)
            return JsonResponse(records_serializer.data, status=200, safe=False)
        pass
