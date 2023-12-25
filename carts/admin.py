from django.contrib import admin

from carts.models import Cart

class CartAdmin(admin.ModelAdmin):
    exclude = []


admin.site.register(Cart, CartAdmin)