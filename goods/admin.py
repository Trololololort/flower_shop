from django.contrib import admin

from .models import Country, Goods, Color, Category

admin.site.register(Category)

admin.site.register(Color)
admin.site.register(Country)


class GoodsAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "name", ]


admin.site.register(Goods, GoodsAdmin)
