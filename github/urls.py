from django.urls import path
from rest_framework.routers import DefaultRouter

# from github.views.github import GithubViewSet
from github.views.auth import GithubAuthAPIView

router = DefaultRouter()

# router.register("/accounts", GithubViewSet),

urlpatterns = [
    path("items/<int:account_id>/get-access-token", GithubAuthAPIView.as_view())
]
