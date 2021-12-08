import base64
import json

import requests

from utils.exceptions import GithubRequestFailed


class GithubAuthService:

    def __init__(self, github):
        self.github = github

    def _check_access_token(self):
        basic_token = base64.b64encode(f"{self.github.client_id}:{self.github.client_secret}".encode("utf-8")).decode("utf-8")
        response = requests.post(
            f"https://api.github.com/applications/{self.github.client_id}/token",
            json={"access_token": self.github.access_token},
            headers={"Authorization": f"Basic {basic_token}"}
        )
        assert response.status_code == 200, "Access token is invalid"

    def _make_request(self, url, body=dict(), headers=dict(), auth=True):
        if auth:
            self._check_access_token()
        try:
            response = json.loads(requests.post(
                url=url,
                json=body,
                headers={**self._default_headers(), **headers}
            ).content)
            assert not response.get("error")
            return response
        except AssertionError as e:
            raise GithubRequestFailed(str(e))

    def _default_headers(self):
        return {
            "Accept": "application/json"
        }

    def get_device_code(self):
        return self._make_request(
            "https://github.com/login/device/code",
            body={
                "client_id": self.github.client_id,
                "scope": self.github.scope
            },
            auth=False
         )

    def get_access_token(self):
        return self._make_request(
            url="https://github.com/login/oauth/access_token",
            body={
                "client_id": self.github.client_id,
                "device_code": self.github.device_code,
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
            },
            auth=False
        )
