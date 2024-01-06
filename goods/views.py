from django.http import Http404, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404

from accounts.models import CustomUser
from goods.models import Goods
from .const import STATUS_CODES
from .forms import GoodsSortFilterForm
from .utils import are_there_enough_goods


class GoodsDetailView(DetailView):
    model = Goods

    def get(self, request, *args, **kwargs):
        # Защититься на случай ввода в
        # адресную строку id товара, которого нет в наличии,
        # хотя, он может быть в админке.
        self.object = get_object_or_404(Goods, pk=kwargs.get("pk"))

        if self.object.stock == 0:
            raise Http404(
                ("Товар отсутствует")
            )

        assert (self.object.stock > 0)

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class GoodsListView(ListView):
    model = Goods
    paginate_by = 5

    def get_queryset(self):
        category = self.request.GET.get("category")
        order_by = self.request.GET.get("order_by")

        queryset = Goods.in_stock.all()

        if order_by and order_by != "--":
            if order_by == 'price' or order_by == 'added':
                # По убыванию цены и даты добавления.
                queryset = queryset.order_by("-" + order_by)

            else:
                assert (order_by == 'category' or order_by == 'origin')
                queryset = queryset.order_by(order_by + "__name")

        if category:
            queryset = queryset.filter(category_id=category)

        return queryset

    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)

        if self.request.GET:
            context_data["sort_filter_form"] = GoodsSortFilterForm(self.request.GET)
        else:
            context_data["sort_filter_form"] = GoodsSortFilterForm()

        return context_data


class AreThereEnoughGoodsToAddToCart(View):

    def post(self, request):
        goods_id = request.POST.get('goods_id')

        enough_goods = are_there_enough_goods(request.user, goods_id)

        if enough_goods:
            result = HttpResponse(STATUS_CODES.ENOUGH.value["message"], status=STATUS_CODES.ENOUGH.value["code"])
        else:
            result = HttpResponse(STATUS_CODES.LACK.value["message"], status=STATUS_CODES.LACK.value["code"])

        return result
