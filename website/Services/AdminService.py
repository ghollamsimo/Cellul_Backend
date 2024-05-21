from website.Repository.Implementations.AdminRepository import AdminRepository


class AdminService:
    def __init__(self):
        self.AdminRepository = AdminRepository()

    def statistics(self):
        return self.AdminRepository.stats()
