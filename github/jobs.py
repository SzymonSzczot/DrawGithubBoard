import time

from django_rq import job

from github.services.authentication import GithubAuthService
from utils.exceptions import GithubRequestFailed


def save_credentials(auth_service, github):
    access_token = auth_service.get_access_token()["access_token"]
    github.access_token = access_token
    github.save()


@job
def poll_access_token(github, threshold=5):
    auth_service = GithubAuthService(github)
    for i in range(15):
        try:
            save_credentials(auth_service, github)
            break
        except GithubRequestFailed as e:
            pass
        time.sleep(threshold)
