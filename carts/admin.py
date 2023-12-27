from django.contrib import admin

from carts.models import Cart

class CartAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "user", "ordered", "status", "goods", "price", "quantity", ]
    list_filter = ["status", "user", ]


admin.site.register(Cart, CartAdmin)