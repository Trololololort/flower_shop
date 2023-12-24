from django.views.generic.base import TemplateView


class AboutCompanyView(TemplateView):
    template_name = "companies/about.html"

class WhereView(TemplateView):
    template_name = "companies/where.html"