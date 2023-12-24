from django.views.generic import DetailView, ListView

from goods.models import Goods


class GoodsDetailView(DetailView):
    model = Goods


class GoodsListView(ListView):
    model = Goods
