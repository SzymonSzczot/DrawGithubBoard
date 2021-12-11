from rest_framework import fields
from rest_framework import serializers

from drawings.models import Pixel
from drawings.utils.parsers import pixel_parse_to_date


class InputPositionField(fields.DateField):

    def to_internal_value(self, date_str):
        """
        For simplicity in JS Template coordinates here are received in format:
        "year_week_weekday"
        """
        return pixel_parse_to_date(date_str)

    def to_representation(self, value):
        return super().to_representation(value)


class PixelCreateSerializer(serializers.ModelSerializer):

    position = InputPositionField()

    class Meta:
        model = Pixel
        fields = (
            "drawing",
            "position"
        )
