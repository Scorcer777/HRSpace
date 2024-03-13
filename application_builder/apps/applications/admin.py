from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'profession',
        'city',
        'salary',
        'number_of_employees',
        'start_working',
    )
