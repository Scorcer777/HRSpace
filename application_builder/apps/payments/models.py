from django.db import models

from . import PAYMENT_TYPES
from apps.applications.models import Application


class Payment(models.Model):
    """Тип оплаты."""

    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    payment_amount = models.BigIntegerField()
    payment_type = models.CharField(max_length=100, choices=PAYMENT_TYPES)
