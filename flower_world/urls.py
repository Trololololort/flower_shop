"""
URL configuration for flower_world project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from companies.views import AboutCompanyView, ContactsView
from django.conf import settings
from django.conf.urls.static import static
from general.views import Test404View
from carts.views import CartDetailView, AddToCart

from goods.views import GoodsDetailView, GoodsListView, IsEnoughInStock
from orders.views import OrdersListView, OrderDetailView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('contacts/', ContactsView.as_view(), name="contacts"),
                  path('about/', AboutCompanyView.as_view(), name="about"),
                  path("goods/<int:pk>/", GoodsDetailView.as_view(), name="goods-detail"),
                  path("goods/", GoodsListView.as_view(), name="goods-list"),
                  path("carts/<int:user>/", CartDetailView.as_view(), name="cart-detail"),
                  path("carts/add/", AddToCart.as_view(), name="add-to-cart"),
                  path("orders/<str:uuid>/", OrderDetailView.as_view(), name="order-detail"),
                  path("orders/", OrdersListView.as_view(), name="orders-list"),
                  path("accounts/", include("accounts.urls")),
                  path("accounts/", include("django.contrib.auth.urls")),
                  path("is-enough-in-stock/", IsEnoughInStock.as_view(), name="is-enough-in-stock"),
                  path("", GoodsListView.as_view(), name="home"),
                  path("test404", Test404View.as_view(), name="test404"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
