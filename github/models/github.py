from django.db import models

from .model_constants import REPO
from .model_constants import SCOPE_CHOICES


class Github(models.Model):
    client_id = models.CharField(max_length=100, default="")
    device_code = models.CharField(max_length=100, default="")
    access_token = models.CharField(max_length=100, default="")
    scope = models.CharField(max_length=20, choices=SCOPE_CHOICES, default=REPO)

    class Meta:
        ordering = ("-id", )
