from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.drawer import DrawTemplateView
from .views.drawing import DrawingViewSet
from .views.pixel import PixelViewSet

router = DefaultRouter()
router.register("items", DrawingViewSet)
router.register("pixels", PixelViewSet)


urlpatterns = [
    path("draw/<int:drawing_id>", DrawTemplateView.as_view(template_name=settings.BASE_DIR + "/templates/drawer/index.html"))
]

urlpatterns += router.urls
