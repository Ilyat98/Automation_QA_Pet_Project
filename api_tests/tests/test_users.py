from api_tests.endpoints import USERS
from api_tests.models.user_model import UsersResponse
from api_tests.payloads.users_payload import create_user_payload


def test_get_users(users_service):
    response = users_service.get_users()
    assert response.status_code == 200
    users = UsersResponse(**response.json())
    assert len(users.data) > 0


def test_create_user(users_service):
    response = users_service.create_user()
    assert response.status_code == 201