from api_tests.endpoints import USERS
from api_tests.services.base_service import BaseService


class UsersService(BaseService):

    def get_users(self):
        return self.api_client.get(USERS)

    def get_user(self, user_id: int):
        return self.api_client.get(f"{USERS}/{user_id}")

    def create_user(self, data: dict):
        return self.api_client.post(USERS, data)

    def update_user(self, user_id: int, data: dict):
        return self.api_client.put(f"{USERS}/{user_id}", data)

    def delete_user(self, user_id: int):
        return self.api_client.delete(f"{USERS}/{user_id}")
