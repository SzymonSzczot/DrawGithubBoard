from django.urls import path
from rest_framework.routers import DefaultRouter

# from github.views.github import GithubViewSet
from .views.auth import GithubAuthAPIView
from .views.update_file import UpdateFileAPIView

router = DefaultRouter()

# router.register("/accounts", GithubViewSet),

urlpatterns = [
    path("items/<int:account_id>/get-access-token", GithubAuthAPIView.as_view()),
    path("items/<int:account_id>/update-file", UpdateFileAPIView.as_view())
]
