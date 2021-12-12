from github.constants import API_URL
from github.services.github import GithubService


class GithubCommitService:

    def __init__(self, github):
        self.service = GithubService(github)
        self.repositories_url = f"{API_URL}/repos/{github.username}/{github.repository}/contents"

    def get_file(self, path):
        return self.service.make_request(
            method="get",
            url=f"{self.repositories_url}/{path}",
            needs_auth=False
        )

    def create_or_update_file(self, path, content):
        file_to_update = self.get_file(path)
        file_sha = file_to_update.get("sha", "")
        return self.service.make_request(
            method="put",
            url=f"{self.repositories_url}/{path}",
            body=self._get_update_body(content, file_sha),
            needs_auth=True
        )

    def _get_update_body(self, content, sha, message="auto"):
        return {
            "content": self.service.convert_string_in_base64(content),
            "sha": sha,
            "message": message
        }
