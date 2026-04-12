import requests
from api_tests.utils.logger import log_request, log_response


class ApiClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"})


    def request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        log_request(method, url, payload=kwargs.get("json"), params=kwargs.get("params"))
        response = self.session.request(method, url, timeout=10, **kwargs)
        log_response(response)
        return response


    def get(self, endpoint, params=None):
        return self.request("GET", endpoint, params=params)


    def post(self, endpoint, payload=None):
        return self.request("POST", endpoint, json=payload)


    def put(self, endpoint, payload=None):
        return self.request("PUT", endpoint, json=payload)


    def delete(self, endpoint):
        return self.request("DELETE", endpoint)