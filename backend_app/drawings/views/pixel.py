from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Pixel
from ..serializers import PixelCreateSerializer
from ..serializers import PixelSerializer
from ..services.matrix import Matrix
from ..services.predict import PredictionService
from ..utils.parsers import pixel_parse_to_date


class PixelViewSet(viewsets.ModelViewSet):
    queryset = Pixel.objects.all()
    serializer_class = PixelSerializer

    def get_pixel(self, position):
        pixel_position = pixel_parse_to_date(position)
        return self.get_queryset().get(position=pixel_position)

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

    def append_prediction(self, response, grid_start):
        prediction_service = PredictionService(grid=grid_start)
        prediction = prediction_service.predict(n_of_results=1)
        matrix = Matrix(prediction["model_result"])
        response.data = {
            **response.data,
            "prediction": prediction,
            "prediction_html": matrix.to_html(rotate=True)
        }
        return response

    def create(self, request, *args, **kwargs):
        """
        Alter POST to allow sending body when deleting Pixel
        """
        if request.data["method"] == "POST":
            response = super().create(request, *args, **kwargs)
            response = self.append_prediction(response, request.data["grid_start"])
            return response
        elif request.data["method"] == "DELETE":
            return self.perform_destroy(self.get_pixel(request.data["position"]))

    def perform_destroy(self, instance):
        instance.delete()
        response = Response(data={}, status=status.HTTP_200_OK)
        return self.append_prediction(response, grid_start=self.request.data["grid_start"])
