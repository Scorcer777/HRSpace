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
    RATING_GRADES,
    NUMBER_OF_COMPLETED_TICKETS,
    RESPONDING_TIME_MINUTES,
    COMPLETING_TICKETS_RATE,
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


class JobInfo(models.Model):
    """Информация об условиях труда."""

    employment_type = models.CharField(
        choices=EMPLOYMENT_TYPES,
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
    work_model = models.CharField(choices=WORK_MODELS, blank=True, null=True)
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


class RecruitRequirements(models.Model):
    """Требования к рекрутеру."""

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    rating = MultiSelectField(
        choices=RATING_GRADES,
        max_choices=len(RATING_GRADES),
        max_length=MAX_LENGTH
    )
    completed_tickets = MultiSelectField(
        choices=NUMBER_OF_COMPLETED_TICKETS,
        max_choices=len(NUMBER_OF_COMPLETED_TICKETS),
        max_length=MAX_LENGTH
    )
    experience = MultiSelectField(
        choices=EXPERIENCES,
        max_choices=len(EXPERIENCES),
        max_length=MAX_LENGTH
    )
    responding_time = MultiSelectField(
        choices=RESPONDING_TIME_MINUTES,
        max_choices=len(RESPONDING_TIME_MINUTES),
        max_length=MAX_LENGTH
    )
    completing_tickets_speed = MultiSelectField(
        choices=COMPLETING_TICKETS_RATE,
        max_choices=len(COMPLETING_TICKETS_RATE),
        max_length=MAX_LENGTH
    )
    industry = models.ForeignKey(
        Industry,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    english_skills = models.CharField(
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
    description = description = models.TextField(
        max_length=MAX_LENGTH,
        blank=True,
        null=True
    )
    candidat_resume_form = models.CharField(
        choices=RESUME_FORM,
        blank=True,
        null=True
    )
    stop_list = models.TextField(max_length=MAX_LENGTH, blank=True, null=True)


class Application(models.Model):
    """Модель заявки."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField()
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    number_of_employees = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    start_working = models.CharField(
        choices=START_WORKING,
        blank=True,
        null=True
    )
    number_of_recruiters = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )
    job_info = models.OneToOneField(JobInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    candidate_requirements = models.OneToOneField(
        CandidateRequirements,
        on_delete=models.CASCADE
    )
    recruit_requirements = models.OneToOneField(
        RecruitRequirements,
        on_delete=models.CASCADE
    )

    def clean(self):
        if self.min_salary > self.max_salary:
            raise ValidationError(
                'Минимальная зарплата не может быть больше максимальной.'
            )
