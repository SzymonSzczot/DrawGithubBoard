import datetime

from rest_framework import viewsets

from ..models import Pixel
from ..serializers import PixelCreateSerializer
from ..serializers import PixelSerializer
from ..utils.parsers import pixel_parse_to_date


class PixelViewSet(viewsets.ModelViewSet):
    queryset = Pixel.objects.all()
    serializer_class = PixelSerializer

    def get_object(self):
        try:
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            pixel_position = pixel_parse_to_date(self.kwargs[lookup_url_kwarg])
            return self.get_queryset().get(position=pixel_position)
        except (Pixel.DoesNotExist, ValueError):
            return super().get_object()

    def get_serializer_class(self):
        if self.action == "create":
            return PixelCreateSerializer
        else:
            return super().get_serializer_class()
