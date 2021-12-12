from django.db import models


class Drawing(models.Model):
    name = models.CharField(max_length=100, default="")

    @property
    def points(self):
        return [pixel.date_coords for pixel in self.pixels.all()]

    @property
    def template_points(self):
        return ["_".join([str(coord) for coord in pixel.date_coords]) for pixel in self.pixels.all()]
