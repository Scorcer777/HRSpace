from django.contrib import admin

from .models import (
    Application,
    JobInfo,
    CandidateRequirements,
    RecruitRequirements,
)
from utils import get_application_id


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'profession',
        'city',
        'min_salary',
        'max_salary',
        'number_of_employees',
        'start_working',
        'number_of_recruiters',
        'created_at',
    )


@admin.register(CandidateRequirements)
class CandidateRequirementsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'application_id',
        'education',
        'experience',
        'get_language_skills',
        'driving_skills',
        'has_photo',
        'get_citizenship',
        'get_core_skills',
    )

    def get_language_skills(self, obj):
        return ', '.join(
            [
                language_proficiency.language.name
                for language_proficiency in obj.language_skills.all()
            ]
        )

    get_language_skills.short_description = 'Language Skills'

    def get_citizenship(self, obj):
        return ', '.join(
            [citizenship.name for citizenship in obj.citizenship.all()]
        )

    get_citizenship.short_description = 'Citizenship'

    def get_core_skills(self, obj):
        return ', '.join(
            [
                profession_skill.skill.title
                for profession_skill in obj.core_skills.all()
            ]
        )

    get_core_skills.short_description = 'Core Skills'

    application_id = get_application_id


@admin.register(JobInfo)
class JobInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'employment_type',
        'schedule',
        'work_model',
        'contract_type',
        'working_conditions',
        'description',
        'application_id',
    )

    application_id = get_application_id


@admin.register(RecruitRequirements)
class RecruitRequirementsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'city',
        'industry',
        'english_skills',
        'recruiter_responsibilities',
        'description',
        'candidate_resume_form',
        'stop_list',
        'application_id',
    )

    application_id = get_application_id
