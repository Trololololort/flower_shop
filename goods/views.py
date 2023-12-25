from django.http import Http404
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from goods.models import Goods
from .forms import GoodsSortFilterForm


class GoodsDetailView(DetailView):
    model = Goods

    def get(self, request, *args, **kwargs):
        # Защититься на случай ввода в
        # адресную строку id товара, которого нет в наличиипше.
        self.object = self.get_object()

        if self.object and not self.object.present:
            raise Http404(
                ("Товар отсутствует")
            )

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class GoodsListView(ListView):
    model = Goods
    paginate_by = 5

    def get_queryset(self):
        category = self.request.GET.get("category")
        order_by = self.request.GET.get("order_by")

        # Пользователю показвать товары: 1) которые есть в наличии; 2) упорядоченные по новизне.
        queryset = super().get_queryset().order_by("-added").filter(present=True)

        if order_by and order_by != "--":
            if order_by == 'price':
                queryset = queryset.order_by(order_by)
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


