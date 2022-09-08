import json

import requests

from . import BadRequest, Forbidden, NotFound, MethodNotAllowed, InternalServerError, Route

BASE = "https://teratail.com/api/v1/"


class HTTPClient:
    def __init__(self, token: str):
        self.token = token

    def request(self, route: Route, **kwargs):
        method = route.method
        url = BASE + route.endpoint
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        data = kwargs.get("data")
        _response = requests.request(method=method, url=url, headers=headers)
        response = _response.json()
        meta = response.get("meta")

        if _response.status_code == 200:
            return response

        if _response.status_code == 400:
            raise BadRequest()

        if _response.status_code == 403:
            raise Forbidden()

        if _response.status_code == 404:
            raise NotFound(f"Your query don't match nothing.")

        if _response.status_code == 405:
            raise MethodNotAllowed()

        if _response.status_code == 500:
            raise InternalServerError("ServerError occured. Retry after.")
