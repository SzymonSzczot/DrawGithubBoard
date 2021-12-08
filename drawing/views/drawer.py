from django.views.generic import TemplateView


class DrawTemplateView(TemplateView):
    permission_classes = []

    def get_context_data(self, **kwargs):
        return {
            "days": 7,
            "weeks": 20
        }
