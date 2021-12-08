from rest_framework import views
from rest_framework.response import Response

from github.jobs import poll_access_token
from github.models import Github
from github.services.authentication import GithubAuthService


class GithubAuthAPIView(views.APIView):

    def get(self, request, account_id, **kwargs):
        github = Github.objects.get(id=account_id)
        auth_service = GithubAuthService(github=github)
        device_code_response = auth_service.get_device_code()
        github.device_code = device_code_response["device_code"]
        poll_access_token.delay(github)
        return Response({"message": "Started polling", **device_code_response})
