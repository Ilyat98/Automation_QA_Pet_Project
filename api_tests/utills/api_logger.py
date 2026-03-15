import json


def log_request(method, url, payload=None, params=None):

    print("\n----- API REQUEST -----")
    print(f"METHOD: {method}")
    print(f"URL: {url}")

    if params:
        print("PARAMS:")
        print(json.dumps(params, indent=4))

    if payload:
        print("PAYLOAD:")
        print(json.dumps(payload, indent=4))


def log_response(response):

    print("----- API RESPONSE -----")
    print(f"STATUS: {response.status_code}")

    try:
        print("BODY:")
        print(json.dumps(response.json(), indent=4))
    except Exception:
        print(response.text)

    print("------------------------\n")