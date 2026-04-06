import requests
from api_tests.utils.api_logger import log_request, log_response



class ApiClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def get(self, endpoint, params=None):
        response = self.session.get(
            f"{self.base_url}{endpoint}",
            params=params,
            timeout=10)
        log_response(response)
        return response

    def post(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        log_request("POST", url, payload)
        response = self.session.post(url, json=payload, timeout=10)
        log_response(response)
        return response

    def put(self, endpoint, payload=None):
        response = self.session.put(
            f"{self.base_url}{endpoint}",
            json=payload,
            timeout=10)
        log_response(response)
        return response

    def delete(self, endpoint):
        response = self.session.delete(
            f"{self.base_url}{endpoint}",
            timeout=10)
        log_response(response)
        return response