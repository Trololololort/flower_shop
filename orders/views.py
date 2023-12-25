from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateOrder(LoginRequiredMixin,
                  View):
    def get(self, request):
        # <view logic>
        context = {"object": "trololo"}
        template_name = "orders/create_order.html"
        return render(request, template_name, context)
    def post(self, request):
        # <view logic>
        context = {"object": "trololo"}
        template_name = "orders/create_order"
        return render(request, template_name, context)


