

def validate_response(response, model=None, status_code=200):
    assert response.status_code == status_code, \
        f"Expected {status_code}, got {response.status_code}. Body: {response.text}"

    if model:
        data = response.json()
        if model == list:
            return data
        try:
            return model(**data)
        except Exception as e:
            raise AssertionError(f"Response validation failed: {e}")

    return response