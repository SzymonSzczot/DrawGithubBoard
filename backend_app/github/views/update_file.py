import json

from rest_framework import views
from rest_framework.response import Response

from github.models import Github
from github.services.commit import GithubCommitService


class UpdateFileAPIView(views.APIView):

    def put(self, request, account_id, **kwargs):
        github = Github.objects.get(id=account_id)
        service = GithubCommitService(github)
        response = service.create_or_update_file(request.data["path"], request.data["content"])
        return Response(response)
