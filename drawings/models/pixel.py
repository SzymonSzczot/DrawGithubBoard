from django.db import models


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
    def coords(self):
        return self.position.isocalendar()
