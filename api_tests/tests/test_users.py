import allure
import pytest
from api_tests.data.user_factory import UserFactory
from api_tests.models.user_model import CreateUserResponse, UpdateUserResponse, User
from api_tests.utils.validator import validate_response


@pytest.mark.api
@pytest.mark.users
@allure.title("Get users list")
def test_get_users(users_service):
    response = users_service.get_users()
    users = validate_response(response, list, 200)
    assert len(users) > 0
    user = users[0]
    assert "id" in user
    assert "name" in user
    assert "email" in user


def test_create_user(users_service):
    payload = UserFactory.user()
    response = users_service.create_user(payload)
    user = validate_response(response, CreateUserResponse, 201)
    assert user.name == payload["name"]


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_single_user(users_service, user_id):
    response = users_service.get_user(user_id)
    user = validate_response(response, User, 200)
    assert user.id == user_id


def test_update_user(users_service, user_data):
    response = users_service.update_user(2, user_data)
    user = validate_response(response, UpdateUserResponse, 200)
    assert user.name == user_data["name"]


def test_delete_user(users_service):
    response = users_service.delete_user(2)
    assert response.status_code == 200


@pytest.mark.parametrize("user_id", [9999, 999999])
def test_get_user_not_found(users_service, user_id):
    response = users_service.get_user(user_id)
    assert response.status_code == 404


def test_users_schema(users_service):
    response = users_service.get_users()
    users = validate_response(response, list, 200)
    for user in users:
        User(**user)