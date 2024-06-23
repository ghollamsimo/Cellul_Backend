from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from website.Serializers.AdviseSerializer import AdviseSerializer
from website.Services.AdviseService import AdviseService


def get_all_advisers(request):
    advise_service = AdviseService()
    advisers = advise_service.index()
    serializer = AdviseSerializer(advisers, many=True, context={'request': request})
    return JsonResponse({'advisers': serializer.data}, safe=False)

def get_advise(request, pk):
    advise_service = AdviseService()
    advise = advise_service.show(pk)
    serializer = AdviseSerializer(advise, context={'request': request})
    return JsonResponse({'advise': serializer.data}, safe=False)

class AdviseView(APIView):
    permission_classes = [AllowAny]

    def patch(self, request, pk, action=None):
        if request.method == 'PATCH':
            advise_service = AdviseService()
            if action == 'appointment_accepted':
                advise_service.appointment(pk, "Accepted")
                return JsonResponse({'message': 'Appointment Has been Accepted'})
            elif action == 'appointment_rejected':
                advise_service.appointment(pk, 'Rejected')
                return JsonResponse({'message': 'Appointment Has been Rejected'})
            else:
                return JsonResponse({'message': 'Invalid action'}, status=400)
        else:
            return JsonResponse({'message': 'Method Not Allowed'}, status=405)
