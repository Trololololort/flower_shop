from django.contrib import admin
from django.contrib import messages

from carts.models import Cart


@admin.action(description="Подтвердить заказ")
def confirm_order(modeladmin, request, queryset):
    # Админ может выбрать любой из элементов в корзине,
    # действие будет применено ко всем элементам.

    # https://stackoverflow.com/questions/11764709/can-you-add-parameters-to-django-custom-admin-actions

    unique_uuids = set(queryset.values_list("order_uuid", flat=True).distinct())

    target_elements = Cart.objects.filter(order_uuid__in=unique_uuids)
    target_elements.update(status="CONFIRMED")

    message = "Подтверждены заказы: {}".format(", ".join([str(elem) for elem in unique_uuids]))
    messages.info(request, message)


class CartAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "user", "order_uuid", "ordered", "status", "goods", "price", "quantity", ]
    list_filter = ["status", "user", "order_uuid", ]
    search_fields = ["order_uuid", ]
    actions = [confirm_order, ]


admin.site.register(Cart, CartAdmin)
