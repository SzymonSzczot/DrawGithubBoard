import datetime

from rest_framework import viewsets

from ..models import Pixel
from ..serializers import PixelCreateSerializer
from ..serializers import PixelSerializer


class PixelViewSet(viewsets.ModelViewSet):
    queryset = Pixel.objects.all()
    serializer_class = PixelSerializer

    def get_object(self):
        try:
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            year, week, weekday = self.kwargs[lookup_url_kwarg].split("_")
            weekday = str(int(weekday) % 7)
            return self.get_queryset().get(position=datetime.datetime.strptime(f"{year}-{week}-{weekday}", "%Y-%W-%w").date())
        except (Pixel.DoesNotExist, ValueError):
            return super().get_object()

    def get_serializer_class(self):
        if self.action == "create":
            return PixelCreateSerializer
        else:
            return super().get_serializer_class()
