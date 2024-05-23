from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from website.Serializers.CalendarSerializer import CalendarSerializer
from website.Services.CalendarService import CalendarService


class CalendarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, action=None):
        if action == 'add_availability':
            return self.add_availability(request)

    def put(self, request, pk, action=None):
        if action == 'update_availability':
            return self.update_availability(request, pk)

    def get(self, request, action=None):
        if action == 'all_availability':
            return self.all_availability(request)

    def delete(self, request, pk, action=None):
        if action == 'delete_availability':
            return self.delete_availability(request, pk)
    def add_availability(self, request):
        if request.method == 'POST':
            calendar_service = CalendarService()
            calendar_service.store(request)
            return JsonResponse({'message': 'Availability Added successfully'}, status=200)
        pass

    def update_availability(self, request, pk):
        if request.method == 'PUT':
            calendar_service = CalendarService()
            calendar_service.update(request, pk)
            return JsonResponse({'message': 'Availability Updated successfully'}, status=200)

        pass

    def all_availability(self, request):
        if request.method == 'GET':
            calendar_service = CalendarService()
            calendar = calendar_service.index(request)
            calendar_serializer = CalendarSerializer(calendar, many=True)
            return JsonResponse(calendar_serializer.data, status=200)
        pass

    def delete_availability(self, request, pk):
        if request.method == 'DELETE':
            calendar_service = CalendarService()
            calendar_service.destroy(request, pk)
            return JsonResponse({'message': 'Availability Deleted successfully'}, status=200)

        pass
