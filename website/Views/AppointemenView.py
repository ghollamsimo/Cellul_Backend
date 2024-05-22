from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from website.Serializers.AppointmentSerializer import AppointmentSerializer
from website.Services.AppointementService import AppointementService
from website.Services.NotificationService import NotificationService


class AppointementView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id, action=None):
        if action == 'add_appointment':
            return self.add_appointment(request, id)
        else:
            return JsonResponse({'message': 'Invalid action'}, status=400)

    def get(self, request, action=None):
        if action == 'all_appointment':
            return self.all_appointments(request)
        return JsonResponse({'message': 'Invalid action'}, status=400)

    def add_appointment(self, request, id):
        if request.method == 'POST':
            appointment_service = AppointementService()
            try:
                appointment = appointment_service.store_appointement(id=id, request=request)
                appointment_dict = model_to_dict(appointment)
                return JsonResponse({'message': 'Appointment Created successfully', 'appointment': appointment_dict})
            except ValueError as e:
                return JsonResponse({'message': str(e)}, status=400)
        else:
            return JsonResponse({'message': 'Method Not Allowed'}, status=405)

    def all_appointments(self, request):
        if request.method == 'GET':
            appointment_service = AppointementService()
            appointments = appointment_service.index_appointement(request)
            appointment_serializer = AppointmentSerializer(appointments, many=True)
            return JsonResponse(appointment_serializer.data, status=200, safe=False)