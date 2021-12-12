from django.db import models

from .model_constants import REPO
from .model_constants import SCOPE_CHOICES


class Github(models.Model):
    username = models.CharField(max_length=100, default="")
    main_repository = models.CharField(max_length=100, default="")
    client_id = models.CharField(max_length=100, default="")
    client_secret = models.CharField(max_length=100, default="")
    device_code = models.CharField(max_length=100, default="")
    access_token = models.CharField(max_length=100, default="")
    scope = models.CharField(max_length=20, choices=SCOPE_CHOICES, default=REPO)

    @property
    def repository(self):
        return self.main_repository

    @repository.setter
    def repository(self, repository):
        self.main_repository = repository
        self.save()

    @repository.getter
    def repository(self):
        # TODO: Allow to choose from repositories? Dynamic?
        return self.main_repository

    class Meta:
        ordering = ("-id", )
