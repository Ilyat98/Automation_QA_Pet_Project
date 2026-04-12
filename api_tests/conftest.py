import pytest
from faker import Faker
from api_tests.client.api_client import ApiClient
from api_tests.endpoints import BASE_URL
from api_tests.services.users_service import UsersService


fake = Faker()


@pytest.fixture
def api_client():
    return ApiClient(BASE_URL)


@pytest.fixture
def users_service(api_client):
    return UsersService(api_client)


@pytest.fixture
def user_data():
    return {
        "name": fake.name(),
        "job": fake.job()
    }