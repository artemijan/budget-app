from django.conf import settings
from django.contrib import admin

# Register your models here.
from core.customer.models import User


class UserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(User, UserAdmin)
