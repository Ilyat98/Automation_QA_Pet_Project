




def assert_status_code(response, expected):

    assert response.status_code == expected, \
        f"Expected {expected}, got {response.status_code}"