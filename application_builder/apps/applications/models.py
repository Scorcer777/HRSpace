from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from django.contrib.postgres.fields import ArrayField
from . import (
    START_WORKING,
    EMPLOYMENT_TYPES, 
    SCHEDULE_TYPES,
    WORK_MODELS,
    CONTRACT_TYPES,
    WORKING_CONDITIONS,
    EDUCATION_TYPES,
    EXPERIENCES,
    DRIVING_SKILLS
)
from apps.professions.models import Profession
from apps.cities.models import City, Citizenship
from apps.languages.models import LanguageProficiency
from apps.users.models import CustomUser


class JobInfo(models.Model):
    """Информация об условиях труда."""

    employment_type = models.CharField(choices=EMPLOYMENT_TYPES)
    schedule = MultiSelectField(
        choices=SCHEDULE_TYPES,
        max_choices=7,
        max_length=1000
    )
    work_model = models.CharField(choices=WORK_MODELS)
    contract_type = MultiSelectField(
        choices=CONTRACT_TYPES,
        max_choices=5,
        max_length=1000
    )
    working_conditions = MultiSelectField(
        choices=WORKING_CONDITIONS,
        max_choices=10,
        max_length=1000
    )


class CandidateRequirements(models.Model):
    """Требования к соискателю."""

    education = MultiSelectField(
        choices=EDUCATION_TYPES,
        max_choices=3,
        max_length=1000
    )
    experience = MultiSelectField(
        choices=EXPERIENCES,
        max_choices=5,
        max_length=1000
    )
    language_skills = models.ManyToManyField(LanguageProficiency)
    driving_skills = MultiSelectField(
        choices=DRIVING_SKILLS,
        max_choices=5,
        max_length=1000
    )
    has_medical_sertificate = models.BooleanField(default=False)
    has_photo = models.BooleanField(default=False)
    citizenship = models.ManyToManyField(Citizenship)
    core_skills = models.TextField()


class Application(models.Model):
    """Модель заявки."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    salary = models.IntegerField()
    number_of_employees = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    start_working = models.CharField(choices=START_WORKING)
    number_of_recruiters = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    job_info = models.OneToOneField(JobInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    candidate_requirements = models.OneToOneField(CandidateRequirements, on_delete=models.CASCADE)
