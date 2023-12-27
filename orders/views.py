from django.views.generic import TemplateView, ListView

from carts.models import Cart


class OrdersListView(ListView):
    model = Cart
    template_name = "orders/order_list.html"
    paginate_by = 5

    def get_queryset(self):
        result = Cart.objects.filter(user=self.request.user).values('order_uuid', "ordered").order_by(
            "-ordered").distinct()
        return result


class OrderDetailView(TemplateView):
    template_name = "orders/order_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
