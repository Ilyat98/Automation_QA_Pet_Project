




def validate_response(response, model):

    try:
        model(**response.json())
    except Exception as e:
        raise AssertionError(
            f"Response validation failed: {e}"
        )