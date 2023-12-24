from django.views.generic.base import TemplateView


class AboutCompanyView(TemplateView):
    template_name = "companies/about_company.html"