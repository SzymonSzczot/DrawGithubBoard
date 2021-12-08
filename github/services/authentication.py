from github.services.github import GithubService


class GithubAuthService:

    def __init__(self, github_account):
        self.service = GithubService(github_account)

    def get_device_code(self):
        return self.service.make_request(
            "https://github.com/login/device/code",
            body={
                "client_id": self.service.github.client_id,
                "scope": self.service.github.scope
            },
            needs_auth=False
         )

    def get_access_token(self):
        return self.service.make_request(
            url="https://github.com/login/oauth/access_token",
            body={
                "client_id": self.service.github.client_id,
                "device_code": self.service.github.device_code,
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
            },
            needs_auth=False
        )
