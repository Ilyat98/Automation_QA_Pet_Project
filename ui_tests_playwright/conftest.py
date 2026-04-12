import pytest
from faker import Faker

fake = Faker()

@pytest.fixture
def generate_login_data():
    fake_email = fake.email()
    fake_pass = fake.password(9)
    return fake_email, fake_pass