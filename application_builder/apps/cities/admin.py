from django.contrib import admin
from .models import City, Citizenship


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Citizenship)
class CitizenshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
