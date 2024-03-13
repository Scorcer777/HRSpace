from django.contrib import admin
from .models import Application, JobInfo, CandidateRequirements


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


@admin.register(CandidateRequirements)
class CandidateRequirementsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'education',
        'experience',
        'get_language_skills',
        'driving_skills',
        'has_medical_sertificate',
        'has_photo',
        'get_citizenship',
        'core_skills',
    )

    def get_language_skills(self, obj):
        return ", ".join(language.name for language in obj.language_skills.all())

    get_language_skills.short_description = 'Language Skills'

    def get_citizenship(self, obj):
        return ", ".join([citizenship.name for citizenship in obj.citizenship.all()])

    get_citizenship.short_description = 'Citizenship'


@admin.register(JobInfo)
class JobInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'employment_type',
        'schedule',
        'work_model',
        'contract_type',
        'working_conditions',
    )
