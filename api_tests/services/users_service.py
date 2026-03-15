from api_tests.endpoints import USERS, SINGLE_USER
from api_tests.payloads.users_payload import create_user_payload
from api_tests.services.base_service import BaseService


class UsersService(BaseService):

    def get_users(self):
        return self.api_client.get(USERS)


    def get_single_user(self, user_id):
        endpoint = SINGLE_USER.format(user_id)
        return self.api_client.get(endpoint)


    def create_user(self, data):
        payload = create_user_payload(data)
        return self.api_client.post(USERS, payload)


    def update_user(self, user_id, data):
        endpoint = SINGLE_USER.format(user_id)
        return self.api_client.put(endpoint, data)


    def delete_user(self, user_id):
        endpoint = SINGLE_USER.format(user_id)
        return self.api_client.delete(endpoint)

