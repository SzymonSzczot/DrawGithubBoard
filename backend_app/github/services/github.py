import base64
import json

import requests

from utils.exceptions import GithubRequestFailed


class GithubService:

    AVAILABLE_METHODS = ["get", "post", "put"]

    def __init__(self, github):
        self.github = github

    def make_request(self, url, body=dict(), headers=dict(), needs_auth=True, method="get"):
        try:
            method = method.lower()
            assert method in self.AVAILABLE_METHODS
            if needs_auth:
                self._check_access_token()
            headers = {**headers, **self._get_auth_headers()}
            response = json.loads(getattr(requests, method)(
                url=url,
                json=body,
                headers={**self._default_headers(), **headers}
            ).content)
            assert not response.get("error")
            return response
        except AssertionError as e:
            raise GithubRequestFailed(str(e))

    def _check_access_token(self):
        response = requests.post(
            f"https://api.github.com/applications/{self.github.client_id}/token",
            json={"access_token": self.github.access_token},
            headers={"Authorization": f"Basic {self._get_basic_token()}"}
        )
        assert response.status_code == 200, "Access token is invalid"

    def _get_basic_token(self):
        credentials = f"{self.github.client_id}:{self.github.client_secret}"
        return self.convert_string_in_base64(credentials)

    def _get_auth_headers(self):
        return {"Authorization": f"token {self.github.access_token}",}

    def _default_headers(self):
        return {"Accept": "application/json"}

    def convert_string_in_base64(self, text):
        return base64.b64encode(text.encode("utf-8")).decode("utf-8")
