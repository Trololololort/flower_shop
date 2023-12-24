from django.views.generic.base import TemplateView


class AboutCompanyView(TemplateView):
    template_name = "companies/about.html"

class ContactsView(TemplateView):
    template_name = "companies/contacts.html"