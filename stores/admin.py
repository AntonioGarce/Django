from django.contrib import admin
from .models import Stores


# Register your models here.
@admin.register(Stores)
class StoreAdmin(admin.ModelAdmin):
    search_fields = ("name",)
