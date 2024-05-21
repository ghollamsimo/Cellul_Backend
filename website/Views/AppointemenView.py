from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import api_view

from website.Services.AppointementService import AppointementService
from website.Services.NotificationService import NotificationService


@api_view(['POST'])
def add_appointment(request, id):
    if request.method == 'POST':
        appointment_service = AppointementService()
        appointment = appointment_service.store_appointement(id=id)

        return JsonResponse({'message': 'Appointment Created successfully', 'appointment': appointment})
    else:
        return JsonResponse({'message': 'Methode Not Allowed'})