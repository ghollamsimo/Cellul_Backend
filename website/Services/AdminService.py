from website.Repository.Implementations.AdminRepository import AdminRepository


class AdminService:
    def __init__(self):
        self.AdminRepository = AdminRepository()

    def statistics(self):
        return self.AdminRepository.stats()

    def update(self, request, id):
        return self.AdminRepository.update_user(request, id)

    def delete(self, request, id):
        return self.AdminRepository.destroy(request, id)
