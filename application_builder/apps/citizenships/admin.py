from django.contrib import admin

from .models import Citizenship


@admin.register(Citizenship)
class CitizenshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
