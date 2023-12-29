from django.contrib import admin

from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    exclude = []


admin.site.register(CustomUser, CustomUserAdmin)
