from rest_framework import viewsets

from ..models import Drawing
from ..serializers import DrawingCreateSerializer
from ..serializers import DrawingSerializer


class DrawingViewSet(viewsets.ModelViewSet):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return DrawingCreateSerializer
        else:
            return super().get_serializer_class()
