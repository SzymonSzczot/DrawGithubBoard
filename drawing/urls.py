from django.conf import settings
from django.urls import path

from drawing.views.drawer import DrawTemplateView

urlpatterns = [
    path("draw", DrawTemplateView.as_view(template_name=settings.BASE_DIR + "/templates/drawer/index.html"))
]
