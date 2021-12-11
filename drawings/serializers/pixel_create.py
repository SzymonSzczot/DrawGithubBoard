import datetime

from rest_framework import fields
from rest_framework import serializers

from drawings.models import Pixel


class InputPositionField(fields.DateField):

    def to_internal_value(self, data):
        """
        For simplicity in JS Template coordinates here are received in format:
        "year_week_weekday"
        """
        year, week, weekday = data.split("_")
        weekday = str(int(weekday) % 7)
        dta = datetime.datetime.strptime(f"{year}-{week}-{weekday}", "%Y-%W-%w").date()
        return dta

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
