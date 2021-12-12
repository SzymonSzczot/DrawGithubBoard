from rest_framework import serializers

from ..models import Pixel


class PixelSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField()
    week = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    def get_day(self, instance):
        return instance.date_coords[2]

    def get_week(self, instance):
        return instance.date_coords[1]

    def get_year(self, instance):
        return instance.date_coords[0]

    class Meta:
        model = Pixel
        fields = ("id", "position", "day", "week", "year", )
        read_only_fields = fields
