from django.contrib import admin

from django.contrib import admin
from django import forms

from .models import *
from dynamic_admin_forms.admin import DynamicModelAdminMixin
from django.contrib.admin.widgets import AdminTextInputWidget


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')


@admin.register(GoodLocation)
class AddCityAdmin(DynamicModelAdminMixin, admin.ModelAdmin):
    dynamic_fields = ('location', 'name')

    def get_dynamic_location_field(self, data):
        queryset = Location.objects.filter(city=data.get("city"))
        value = data.get('location')

        if value not in queryset:
            value = queryset.first()

        hidden = False

        return queryset, value, hidden

    def get_dynamic_full_name_field(self, data):
        value = data.get("name", "") + " " + data.get("city", "")
        return None, value, False


class AddCityInline(DynamicModelAdminMixin, admin.TabularInline):
    model = GoodLocation
    dynamic_fields = ('location', 'full_name')

    def get_dynamic_location_field(self, data):
        queryset = Location.objects.filter(city=data.get("city"))
        value = data.get('location')

        if value not in queryset:
            value = queryset.first()

        hidden = False

        return queryset, value, hidden

    def get_dynamic_full_name_field(self, data):
        value = data.get("name", "") + " " + data.get("city", "")
        return None, value, False


@admin.register(Goods)
class Goods(DynamicModelAdminMixin, admin.ModelAdmin):
    inlines = [AddCityInline]
    search_fields = ("name",)
    class Meta:
        model = Goods


admin.site.register(Comments)