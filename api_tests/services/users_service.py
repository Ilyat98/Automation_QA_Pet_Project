from api_tests.endpoints import USERS
from api_tests.services.base_service import BaseService


class UsersService(BaseService):

    def get_users(self):
        return self.api_client.get(USERS)


    def get_single_user(self, user_id):
        return self.api_client.get(f"{USERS}/{user_id}")


    def create_user(self, payload):
        return self.api_client.post(USERS, payload)


    def update_user(self, user_id, payload):
        return self.api_client.put(f"{USERS}/{user_id}", payload)


    def delete_user(self, user_id):
        return self.api_client.delete(f"{USERS}/{user_id}")

