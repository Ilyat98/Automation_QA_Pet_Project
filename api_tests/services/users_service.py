from api_tests.endpoints import USERS
from api_tests.payloads.users_payload import create_user_payload


class UsersService:

    def __init__(self, api_client):
        self.api_client = api_client


    def get_users(self):
        return self.api_client.get(USERS)


    def create_user(self):
        payload = create_user_payload()
        return self.api_client.post(USERS, payload)