from api_tests.models.user_model import User

def validate_users_response(response):
    data = response.json()
    return [User(**item) for item in data]