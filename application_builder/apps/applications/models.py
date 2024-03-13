from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from . import (
    START_WORKING,
    EMPLOYMENT_TYPES, 
    SCHEDULE_TYPES,
    WORK_MODELS,
    CONTRACT_TYPES,
    WORKING_CONDITIONS,
)
from apps.professions.models import Profession
from apps.cities.models import City


class Application(models.Model):
    """Заявка на поиск рекрутера."""

    #user = models.
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
    employment_type = models.CharField(choices=EMPLOYMENT_TYPES)
    schedule = models.ManyToManyField(choices=SCHEDULE_TYPES)
    work_model = models.CharField(choices=WORK_MODELS)
    contract_type = models.ManyToManyField(choices=CONTRACT_TYPES)
    working_conditions = models.ManyToManyField(choices=WORKING_CONDITIONS)
