from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "added", "cart", ]


admin.site.register(Order, OrderAdmin)
