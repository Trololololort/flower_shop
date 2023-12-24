from django.views.generic import DetailView, ListView

from goods.models import Goods


class GoodsDetailView(DetailView):
    model = Goods


class GoodsListView(ListView):
    model = Goods

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset
