from django.views.generic.base import TemplateView

from goods.models import Goods


class AboutCompanyView(TemplateView):
    template_name = "companies/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Goods.in_stock.all()[:5]
        return context


class ContactsView(TemplateView):
    template_name = "companies/contacts.html"
