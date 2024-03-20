from django.contrib import admin

from .models import (
    Application,
    JobInfo,
    CandidateRequirements,
    RecruitRequirements,
)


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
        'application',
        'education',
        'experience',
        'get_language_skills',
        'driving_skills',
        'has_photo',
        'get_citizenships',
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

    def get_citizenships(self, obj):
        return ', '.join(
            [citizenship.name for citizenship in obj.citizenship.all()]
        )

    get_citizenships.short_description = 'Citizenship'

    def get_core_skills(self, obj):
        return ', '.join(
            [
                profession_skill.skill.title
                for profession_skill in obj.core_skills.all()
            ]
        )

    get_core_skills.short_description = 'Core Skills'


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
        'application',
    )


@admin.register(RecruitRequirements)
class RecruitRequirementsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'industry',
        'english_skills',
        'recruiter_responsibilities',
        'description',
        'candidate_resume_form',
        'stop_list',
        'application',
    )
