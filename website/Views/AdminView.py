from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from website.Services.AdminService import AdminService


class AdminView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, action=None):
        if request.method == 'GET' and action == 'all_stats':
            return self.get_stats()
        pass

    def patch(self, request, id, action=None):
        if action == 'update_user':
            return self.update_user(request, id)

    def delete(self, request, id, action=None):
        if action == 'delete_user':
            return self.delete_user(request, id)

    def get_stats(self):
        admin_service = AdminService()
        stats = admin_service.statistics()
        return JsonResponse(stats)
        pass

    def update_user(self, request, id):
        if request.method == 'PATCH':
            admin_service = AdminService()
            admin_service.update(request, id)
            return JsonResponse({'message': 'User Updated Successfully'})
        pass

    def delete_user(self, request, id):
        if request.method == 'DELETE':
            admin_service = AdminService()
            admin_service.delete(request, id)
            return JsonResponse({'message': 'User Deleted Successfully'}, safe=True)