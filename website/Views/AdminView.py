from django.http import JsonResponse
from rest_framework.views import APIView

from website.Services.AdminService import AdminService


class AdminView(APIView):

    def get(self, request, action=None):
        if request.method == 'GET' and action == 'all_stats':
            return self.get_stats()
        pass

    def get_stats(self):
        admin_service = AdminService()
        stats = admin_service.statistics()
        return JsonResponse(stats)
        pass