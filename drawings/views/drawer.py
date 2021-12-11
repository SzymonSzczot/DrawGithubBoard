from django.views.generic import TemplateView

from drawings.models import Drawing


class DrawTemplateView(TemplateView):
    permission_classes = []

    def get_context_data(self, drawing_id, **kwargs):
        drawing = Drawing.objects.get(id=drawing_id)
        return {
            "drawing": drawing,
            "points": drawing.template_points,
        }
