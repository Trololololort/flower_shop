from django.contrib import admin

from .models import Country, Goods, Type, Color, Package, Extra, Category

admin.site.register(Extra)
admin.site.register(Category)
admin.site.register(Package)
admin.site.register(Type)
admin.site.register(Color)
admin.site.register(Country)



class GoodsAdmin(admin.ModelAdmin):
    exclude = []
    list_display = ["id", "name", ]


admin.site.register(Goods, GoodsAdmin)