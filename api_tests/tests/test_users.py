import allure
import pytest
from api_tests.factories.user_factory import UserFactory
from api_tests.models.user_model import CreateUserResponse, UsersResponse
from api_tests.utills.assertions import assert_status_code
from api_tests.utills.response_validator import validate_response
from utils.validators import validate_users_response


@pytest.mark.api
@pytest.mark.users
@allure.title("Get users list")
def test_get_users(users_service):
    response = users_service.get_users()
    assert_status_code(response, 200)
    users = validate_response(response, UsersResponse)
    assert users.page == 1
    assert len(users.data) > 0


def test_create_user(users_service):
    payload = {
        "name": "John",
        "job": "QA"
    }
    response = users_service.create_user(payload)
    user = validate_response(response, CreateUserResponse)
    assert user.name == payload["name"]


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_single_user(users_service, user_id):
    response = users_service.get_single_user(user_id)
    assert_status_code(response, 200)
    data = response.json()
    assert data["data"]["id"] == user_id


def test_update_user(users_service, generate_user_data):
    response = users_service.update_user(2, generate_user_data)
    assert_status_code(response, 200)
    data = response.json()
    assert "name" in data
    assert "job" in data



def test_delete_user(users_service):
    response = users_service.delete_user(2)
    assert_status_code(response, 204)


def test_get_user_not_found(users_service):
    response = users_service.get_single_user(9999)
    assert_status_code(response, 404)


@pytest.mark.parametrize("payload", [{}, {"name": 123}, {"job": None}])
def test_create_user_invalid_payload(users_service, payload):
    response = users_service.create_user(payload)
    assert response.status_code >= 400


def test_users_pagination(users_service):
    response = users_service.get_users()
    data = response.json()
    assert data["page"] == 1
    assert data["per_page"] > 0