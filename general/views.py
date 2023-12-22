from django.views.generic.base import TemplateView


class AboutCompanyView(TemplateView):
    template_name = "general/parts/header.html"
