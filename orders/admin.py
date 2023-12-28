from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "ordered", "status", ]
    list_filter = ["status", "user", "id", ]
    search_fields = ["order_uuid", ]


admin.site.register(Order, OrderAdmin)
