from django.contrib import admin

from carts.models import Cart


class CartAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "user", "order_uuid", "ordered", "status", "goods", "price", "quantity", ]
    list_filter = ["status", "user", "order_uuid", ]
    search_fields = ["order_uuid", ]


admin.site.register(Cart, CartAdmin)
