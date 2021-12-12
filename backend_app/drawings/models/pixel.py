from django.db import models

from ..utils.parsers import pixel_parse_to_identifier


class Pixel(models.Model):
    drawing = models.ForeignKey(
        "drawings.Drawing",
        on_delete=models.CASCADE,
        null=False,
        related_name="pixels"
    )
    # This is position of Pixel drawn. Coords looks like this:
    # x = position.week, y = position.weekday
    position = models.DateField(unique=True)

    @property
    def date_coords(self):
        return pixel_parse_to_identifier(self.position)
