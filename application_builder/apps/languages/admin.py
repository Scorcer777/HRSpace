from django.contrib import admin

from .models import Language, LanguageProficiency


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(LanguageProficiency)
class LanguageProficiencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'language', 'proficiency_level')
