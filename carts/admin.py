from django.contrib import admin

from carts.models import Cart


class CartAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "user", "order", "goods", "price", "quantity", ]


admin.site.register(Cart, CartAdmin)
