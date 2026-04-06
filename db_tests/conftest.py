import pytest
from db_tests.db_client import DBClient


@pytest.fixture
def db_client():

    client = DBClient()
    yield client
    client.close()