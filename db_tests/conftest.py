from uuid import uuid4
import pytest
from db_tests.db_client import DBClient


@pytest.fixture
def db_client():
    client = DBClient()
    yield client
    client.close()


@pytest.fixture
def user_email():
    return f"test_{uuid4()}@test.com"