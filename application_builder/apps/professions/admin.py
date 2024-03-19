from django.contrib import admin

from .models import Profession, Skill, ProfessionSkill


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'industry',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(ProfessionSkill)
class ProfessionSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'skill',)
