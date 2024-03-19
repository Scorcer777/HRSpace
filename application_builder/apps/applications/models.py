from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError

from . import (
    MAX_LENGTH,
    START_WORKING,
    EMPLOYMENT_TYPES, 
    SCHEDULE_TYPES,
    WORK_MODELS,
    CONTRACT_TYPES,
    WORKING_CONDITIONS,
    EDUCATION_TYPES,
    EXPERIENCES,
    DRIVING_SKILLS,
    RECRUITER_RESPONSIBILITIES,
    RESUME_FORM,
)
from apps.professions.models import Profession, ProfessionSkill
from apps.cities.models import City
from apps.citizenships.models import Citizenship
from apps.languages.models import LanguageProficiency
from apps.users.models import CustomUser
from apps.languages import LEVEL_CHOICES
from apps.industries.models import Industry


class Application(models.Model):
    """Модель заявки."""

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    title = models.CharField(max_length=100,)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    min_salary = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(0)]
    )
    max_salary = models.IntegerField(
        blank=False,
        validators=[MinValueValidator(0)]
    )
    number_of_employees = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    start_working = models.CharField(
        max_length=100,
        choices=START_WORKING,
        blank=True,
        null=True
    )
    number_of_recruiters = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.min_salary > self.max_salary:
            raise ValidationError(
                'Минимальная зарплата не может быть больше максимальной.'
            )

    def __str__(self) -> str:
        return self.title


class JobInfo(models.Model):
    """Информация об условиях труда."""

    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name='job_infos'
    )
    employment_type = MultiSelectField(
        choices=EMPLOYMENT_TYPES,
        max_choices=len(EMPLOYMENT_TYPES),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    schedule = MultiSelectField(
        choices=SCHEDULE_TYPES,
        max_choices=len(SCHEDULE_TYPES),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    work_model = MultiSelectField(
        choices=WORK_MODELS,
        max_choices=len(WORK_MODELS),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    contract_type = MultiSelectField(
        choices=CONTRACT_TYPES,
        max_choices=len(CONTRACT_TYPES),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    working_conditions = MultiSelectField(
        choices=WORKING_CONDITIONS,
        max_choices=len(WORKING_CONDITIONS),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    description = models.TextField(
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )


class CandidateRequirements(models.Model):
    """Требования к соискателю."""

    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name='candidate_requirements'
    )
    education = MultiSelectField(
        choices=EDUCATION_TYPES,
        max_choices=len(EDUCATION_TYPES),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    experience = MultiSelectField(
        choices=EXPERIENCES,
        max_choices=len(EXPERIENCES),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    language_skills = models.ManyToManyField(
        LanguageProficiency,
        blank=True,
    )
    driving_skills = MultiSelectField(
        choices=DRIVING_SKILLS,
        max_choices=len(DRIVING_SKILLS),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    has_medical_sertificate = models.BooleanField(
        default=False,
        blank=True,
        null=True
    )
    has_photo = models.BooleanField(default=False, blank=True, null=True)
    citizenship = models.ManyToManyField(Citizenship, blank=True)
    core_skills = models.ManyToManyField(
        ProfessionSkill,
        blank=True
    )
    requirements_description = models.TextField(blank=True, null=True)


class RecruitRequirements(models.Model):
    """Требования к рекрутеру."""

    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name='recruit_requirements'
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    industry = models.ForeignKey(
        Industry,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    english_skills = models.CharField(
        max_length=100,
        choices=LEVEL_CHOICES,
        blank=True,
        null=True
    )
    recruiter_responsibilities = MultiSelectField(
        choices=RECRUITER_RESPONSIBILITIES,
        max_choices=len(RECRUITER_RESPONSIBILITIES),
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    description = models.TextField(
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    candidate_resume_form = models.CharField(
        max_length=100,
        choices=RESUME_FORM,
        blank=True,
        null=True
    )
    stop_list = models.TextField(max_length=MAX_LENGTH, blank=True, null=True)
