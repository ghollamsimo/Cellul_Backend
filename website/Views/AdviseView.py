from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from website.Services.AdviseService import AdviseService


class AdviseView(APIView):
    permission_classes = [AllowAny]

    def patch(self, request, pk, action=None):
        if request.method == 'PATCH':
            advise_service = AdviseService()
            if action == 'appointment_accepted':
                advise_service.appointment(pk,"Accepted")
                return JsonResponse({'message': 'Appointment Has been Accepted'})
            elif action == 'appointment_rejected':
                advise_service.appointment(pk, 'Rejected')
                return JsonResponse({'message': 'Appointment Has been Rejected'})
            else:
                return JsonResponse({'message': 'Invalid action'}, status=400)
        else:
            return JsonResponse({'message': 'Method Not Allowed'}, status=405)
