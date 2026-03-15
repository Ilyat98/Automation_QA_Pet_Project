import pytest
from faker import Faker
from api_tests.api_client.client import ApiClient
from api_tests.endpoints import BASE_URL
from api_tests.services.users_service import UsersService


fake = Faker()

@pytest.fixture
def api_client():
    base_url = BASE_URL
    return ApiClient(base_url)


@pytest.fixture
def users_service(api_client):
    return UsersService(api_client)


@pytest.fixture
def generate_user_data():
    return {
        "name": fake.name(),
        "job": fake.job()
    }