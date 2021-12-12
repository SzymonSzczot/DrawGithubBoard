from rest_framework import serializers

from .pixel import PixelSerializer
from ..models import Drawing


class DrawingSerializer(serializers.ModelSerializer):
    pixels = PixelSerializer(many=True, data=list)

    class Meta:
        model = Drawing
        fields = (
            "id",
            "name",
            "pixels",
        )
        read_only_fields = ("pixels", )
