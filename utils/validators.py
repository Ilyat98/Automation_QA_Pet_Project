from api_tests.models.user_model import UsersResponse


def validate_users_response(response):
    return UsersResponse(**response.json())