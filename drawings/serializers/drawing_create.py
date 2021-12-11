from rest_framework import serializers

from drawings.models import Drawing


class DrawingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drawing
        fields = ("name", )
