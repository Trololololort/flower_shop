from django.views.generic import TemplateView

class Test404View(TemplateView):
    # Только для тестирования внешнего вида страницы 404.
    template_name = "404.html"
